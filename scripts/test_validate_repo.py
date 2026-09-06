#!/usr/bin/env python3
"""One runnable regression check: valid repository, then isolated invalid mutations."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from validate_repo import ROOT, validate


def main() -> None:
    assert not validate(ROOT), validate(ROOT)
    assert not (ROOT / "archive").exists(), "archive must not ship in the release tree"
    with TemporaryDirectory() as temporary:
        root = Path(temporary)
        skill = root / "sample"
        skill.mkdir()
        original = {
            "MANIFEST.json": json.dumps({"version": "2.1.0", "skills": ["sample"]}),
            "sample/SKILL.md": "---\nname: sample\nversion: 2.1.0\ndescription: Useful sample\n---\n# Sample\nFollow the user's task.\n",
            "sample/test-prompts.json": json.dumps({"skill": "sample", "cases": [
                {"id": "ordinary", "prompt": "Write a scene.", "expect": "Follow the request."}
            ]}),
            "README.md": "[Sample](sample/SKILL.md)\n",
        }

        def restore() -> None:
            for name, content in original.items():
                (root / name).write_text(content, encoding="utf-8")

        restore()
        assert not validate(root), validate(root)
        mutations = [
            ("sample/SKILL.md", "---\nname: sample\nversion: 2.1.0\ndescription: synthetic placeholder\n---\n# Sample\n", "placeholder"),
            ("sample/SKILL.md", "---\nname: sample\nversion: 2.1.0\ndescription: Sample\n---\n# Sample\n", "instructional body"),
            ("sample/test-prompts.json", '{"skill":"sample","cases":[]}', "non-empty list"),
            ("sample/test-prompts.json", '{"skill":"sample","cases":[{}]}', "prompt"),
            ("sample/test-prompts.json", '[]', "must be an object"),
            ("sample/test-prompts.json", '{', "cannot read JSON"),
            ("README.md", "[Missing](sample/missing.md)\n", "broken internal link"),
            ("MANIFEST.json", '{"version":"2.1.0","skills":["../archive"]}', "safe kebab-case"),
            ("MANIFEST.json", '{"version":"2.1.0","skills":["sample","sample"]}', "duplicate skill IDs"),
        ]
        for name, content, expected in mutations:
            restore()
            (root / name).write_text(content, encoding="utf-8")
            errors = validate(root)
            assert any(expected in error for error in errors), (name, errors)
        restore()
        (skill / "test-prompts.json").unlink()
        assert any("cannot read JSON" in error for error in validate(root))
        restore()
        (root / "tests").mkdir()
        (root / "tests" / "cross.json").write_text('{"cases":[{"id":"x","prompt":"p","must":[],"must_not":["bad"]}]}', encoding="utf-8")
        assert any("must must be a non-empty list" in error for error in validate(root))
    print("Validator self-check OK: archive-free repository and 11 invalid scenarios.")


if __name__ == "__main__":
    main()
