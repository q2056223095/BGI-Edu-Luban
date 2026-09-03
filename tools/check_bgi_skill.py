#!/usr/bin/env python3
"""Static repository checker for BGI Edu AI assets.

This tool checks repository structure and a few safety signals. It does NOT
replace real regression tests, scientific review, or release approval.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


@dataclass
class Check:
    id: str
    level: str  # PASS/WARN/FAIL
    message: str
    path: str | None = None


REQUIRED_FILES = ["SKILL.md", "README.md"]
RECOMMENDED_FILES = ["VERSION", "CHANGELOG.md"]
RECOMMENDED_DIRS = [
    "references",
    "examples",
    "tests/regression",
    "tests/golden",
    "tests/adversarial",
]

SECRET_PATTERNS = [
    ("openai_like_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("bearer_token", re.compile(r"Authorization\s*:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}", re.I)),
]

TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".py", ".js", ".ts",
    ".html", ".css", ".sh", ".ps1", ".bat", ".ini", ".cfg"
}


def read_text(path: Path) -> str:
    try:
        if path.stat().st_size > 1_000_000:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def check_frontmatter(skill_path: Path) -> list[Check]:
    out: list[Check] = []
    text = read_text(skill_path)
    if not text:
        return [Check("frontmatter", "FAIL", "SKILL.md is empty or unreadable", str(skill_path))]
    if not text.startswith("---"):
        out.append(Check("frontmatter", "WARN", "SKILL.md has no YAML-style frontmatter", str(skill_path)))
        return out
    head = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    for key in ("name:", "description:"):
        if key not in head:
            out.append(Check(f"frontmatter_{key[:-1]}", "WARN", f"frontmatter missing {key[:-1]}", str(skill_path)))
        else:
            out.append(Check(f"frontmatter_{key[:-1]}", "PASS", f"frontmatter contains {key[:-1]}", str(skill_path)))
    return out


def iter_text_files(root: Path) -> Iterable[Path]:
    skip = {".git", "node_modules", ".venv", "venv", "dist", "build"}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in skip for part in p.parts):
            continue
        if p.suffix.lower() in TEXT_SUFFIXES or p.name in {"VERSION", "LICENSE"}:
            yield p


def scan_secrets(root: Path) -> list[Check]:
    findings: list[Check] = []
    for path in iter_text_files(root):
        text = read_text(path)
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(Check(
                    f"secret_{name}",
                    "FAIL",
                    f"possible secret detected: {name}",
                    str(path.relative_to(root)),
                ))
    if not findings:
        findings.append(Check("secret_scan", "PASS", "no obvious secret patterns detected"))
    return findings


def run(root: Path, do_secret_scan: bool) -> list[Check]:
    checks: list[Check] = []
    if not root.exists() or not root.is_dir():
        return [Check("root", "FAIL", f"target is not a directory: {root}")]

    for name in REQUIRED_FILES:
        p = root / name
        if p.exists():
            checks.append(Check(f"file_{name}", "PASS", f"required file present: {name}", name))
        else:
            checks.append(Check(f"file_{name}", "FAIL", f"required file missing: {name}", name))

    for name in RECOMMENDED_FILES:
        p = root / name
        if p.exists():
            checks.append(Check(f"file_{name}", "PASS", f"recommended file present: {name}", name))
        else:
            checks.append(Check(f"file_{name}", "WARN", f"recommended file missing: {name}", name))

    for name in RECOMMENDED_DIRS:
        p = root / name
        if p.exists() and p.is_dir():
            checks.append(Check(f"dir_{name}", "PASS", f"recommended directory present: {name}", name))
        else:
            checks.append(Check(f"dir_{name}", "WARN", f"recommended directory missing: {name}", name))

    skill = root / "SKILL.md"
    if skill.exists():
        checks.extend(check_frontmatter(skill))

    # Regression / Golden minimum signals.
    reg_dir = root / "tests" / "regression"
    if reg_dir.exists():
        case_files = [p for p in reg_dir.iterdir() if p.is_file() and p.name.lower() != "readme.md"]
        level = "PASS" if len(case_files) >= 3 else "WARN"
        checks.append(Check("regression_count", level, f"regression case files: {len(case_files)}", "tests/regression"))

    golden_dir = root / "tests" / "golden"
    if golden_dir.exists():
        case_files = [p for p in golden_dir.iterdir() if p.is_file() and p.name.lower() != "readme.md"]
        level = "PASS" if len(case_files) >= 1 else "WARN"
        checks.append(Check("golden_count", level, f"golden case files: {len(case_files)}", "tests/golden"))

    if do_secret_scan:
        checks.extend(scan_secrets(root))

    return checks


def summarize(checks: list[Check]) -> str:
    levels = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for c in checks:
        levels[c.level] = levels.get(c.level, 0) + 1
    if levels["FAIL"]:
        status = "FAIL"
    elif levels["WARN"]:
        status = "WARN"
    else:
        status = "PASS"
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a BGI Edu AI asset repository")
    parser.add_argument("target", nargs="?", default=".", help="target repository path")
    parser.add_argument("--json", action="store_true", help="output JSON")
    parser.add_argument("--scan-secrets", action="store_true", help="scan text files for obvious credential patterns")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    checks = run(root, args.scan_secrets)
    status = summarize(checks)

    if args.json:
        print(json.dumps({
            "target": str(root),
            "status": status,
            "checks": [asdict(c) for c in checks],
            "note": "Static check only; does not replace regression/scientific/brand review."
        }, ensure_ascii=False, indent=2))
    else:
        print(f"BGI Edu Skill Check: {root}")
        print(f"STATUS: {status}\n")
        for c in checks:
            where = f" [{c.path}]" if c.path else ""
            print(f"{c.level:4} {c.id}: {c.message}{where}")
        print("\nNOTE: Static check only; real QA still requires Risk Gates and Regression evidence.")

    return 2 if status == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
