#!/usr/bin/env python3
"""Validate active skill files and cases, not literary or medical quality."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FIELDS = re.compile(r"^([\w-]+):[ \t]*(.*?)[ \t]*$", re.M)
# ponytail: inline links only; use a Markdown parser if reference links become necessary.
LINKS = re.compile(r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
PLACEHOLDER = re.compile(r"synthetic placeholder|PLACEHOLDER::", re.I)
SKILL_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def fail(path: Path, message: str) -> None:
        errors.append(f"{path.relative_to(root)}: {message}")

    def read_json(path: Path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            fail(path, f"cannot read JSON: {exc}")
            return None

    def check_cases(path: Path, data, local_skill: str | None = None) -> None:
        if not isinstance(data, dict):
            fail(path, "test data must be an object")
            return
        if local_skill is not None and data.get("skill") != local_skill:
            fail(path, f"skill must equal {local_skill!r}")
        cases = data.get("cases")
        if not isinstance(cases, list) or not cases:
            fail(path, "cases must be a non-empty list")
            return
        seen: set[str] = set()
        for index, case in enumerate(cases, 1):
            if not isinstance(case, dict):
                fail(path, f"case {index} must be an object")
                continue
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id.strip():
                fail(path, f"case {index}: missing non-empty id")
            elif case_id in seen:
                fail(path, f"duplicate case id {case_id!r}")
            else:
                seen.add(case_id)
            keys = ("prompt", "expect") if local_skill else ("prompt",)
            for key in keys:
                if not isinstance(case.get(key), str) or not case[key].strip():
                    fail(path, f"case {index}: {key} must be non-empty text")
            if local_skill is None:
                for key in ("must", "must_not"):
                    values = case.get(key)
                    if not isinstance(values, list) or not values or not all(
                        isinstance(value, str) and value.strip() for value in values
                    ):
                        fail(path, f"case {index}: {key} must be a non-empty list of text")

    manifest = read_json(root / "MANIFEST.json")
    if not isinstance(manifest, dict):
        return errors or ["MANIFEST.json: must be an object"]
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills or not all(
        isinstance(skill, str) and skill != "archive" and SKILL_ID.fullmatch(skill) for skill in skills
    ):
        return errors + ["MANIFEST.json: skills must be non-empty safe kebab-case IDs"]
    if len(skills) != len(set(skills)):
        errors.append("MANIFEST.json: duplicate skill IDs")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        errors.append("MANIFEST.json: version must be semantic x.y.z")

    for skill in skills:
        path = root / skill / "SKILL.md"
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            fail(path, f"missing or unreadable SKILL.md: {exc}")
            continue
        match = FRONTMATTER.match(text)
        fields = dict(FIELDS.findall(match.group(1))) if match else {}
        if not match:
            fail(path, "missing frontmatter")
        if fields.get("name") != skill:
            fail(path, f"name must equal {skill!r}")
        for key in ("version", "description"):
            if not fields.get(key):
                fail(path, f"missing {key}")
        body = text[match.end():] if match else ""
        if not any(line.strip() and not line.lstrip().startswith("#") for line in body.splitlines()):
            fail(path, "missing instructional body")
        if PLACEHOLDER.search(text):
            fail(path, "placeholder content is not an active skill")
        tests = root / skill / "test-prompts.json"
        check_cases(tests, read_json(tests), skill)

    for path in sorted((root / "tests").glob("*.json")):
        check_cases(path, read_json(path))
    for name in ("MEM-Base", "skill-SAK-v2", "skill-SAE-v2", "skill-OOE-v2", "skill-义眼-v2"):
        if (root / name).exists():
            errors.append(f"{name}: superseded runtime directory at root")

    # Historical source paths are prose only; current runtime links must resolve inside this tree.
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts) or relative.parts[0] == "archive":
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        for raw in LINKS.findall(text):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (path.parent / unquote(target.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                fail(path, f"broken internal link: {raw}")
    return errors


def main() -> int:
    errors = validate(ROOT)
    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        print(f"Validation failed: {len(errors)} error(s).")
        return 1
    print("Validation OK: active skills, non-empty cases and internal file links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
