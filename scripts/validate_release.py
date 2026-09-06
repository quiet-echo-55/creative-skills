#!/usr/bin/env python3
"""Release-level checks: semver, active naming, and archive-free release hygiene."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FIELDS = re.compile(r"^([\w-]+):[ \t]*(.*?)[ \t]*$", re.M)
SEMVER = re.compile(r"\d+\.\d+\.\d+")
PRIVATE_ACTIVE = re.compile(r"Standlone\s+MEM|Standalone\s+MEM|MEM\s*创作", re.I)
OPAQUE_ACTIVE = re.compile(r"(^|[^A-Za-z])(SAK|SAE|OOE)([^A-Za-z]|$)")


def main() -> int:
    errors: list[str] = []
    manifest_path = ROOT / "MANIFEST.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: MANIFEST.json unreadable: {exc}")
        return 1

    version = str(manifest.get("version", ""))
    if not SEMVER.fullmatch(version):
        errors.append(f"MANIFEST.json: invalid semantic version {version!r}")

    skills = manifest.get("skills")
    if not isinstance(skills, list):
        errors.append("MANIFEST.json: skills must be a list")
        skills = []

    for skill in skills:
        skill_dir = ROOT / str(skill)
        path = skill_dir / "SKILL.md"
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path.relative_to(ROOT)}: unreadable: {exc}")
            continue
        match = FRONTMATTER.match(text)
        fields = dict(FIELDS.findall(match.group(1))) if match else {}
        skill_version = fields.get("version", "")
        if skill_version != version:
            errors.append(f"{path.relative_to(ROOT)}: version {skill_version!r} != manifest {version!r}")
        for active_file in skill_dir.rglob("*"):
            if not active_file.is_file() or active_file.stat().st_size > 2_000_000:
                continue
            try:
                active_text = active_file.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if PRIVATE_ACTIVE.search(active_text):
                errors.append(f"{active_file.relative_to(ROOT)}: private/legacy branding remains in active runtime")
            if OPAQUE_ACTIVE.search(active_text):
                errors.append(f"{active_file.relative_to(ROOT)}: opaque legacy runtime acronym remains")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    major_minor = ".".join(version.split(".")[:2]) if SEMVER.fullmatch(version) else ""
    if major_minor and f"# Creative Skills {major_minor}" not in readme:
        errors.append("README.md: release heading does not match MANIFEST major.minor")

    if (ROOT / "archive").exists():
        errors.append("archive/: historical source material must not ship in the release tree")

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        print(f"Release validation failed: {len(errors)} error(s).")
        return 1

    print("Release validation OK: semver, active naming, and archive-free release hygiene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
