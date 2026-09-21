#!/usr/bin/env python3
"""
Auto-maintain mdBook SUMMARY.md from src/ tree.
Keeps existing entries intact, appends only missing ones.
Supports nested directories and Chinese folder names.
"""

from pathlib import Path

SRC = Path("src")
SUMMARY = SRC / "SUMMARY.md"
EXCLUDED = {"README.md", "SUMMARY.md"}


def clean_title(value: str) -> str:
    value = value.replace("_", " ")
    if value.endswith(".md"):
        value = value[:-3]
    return value.strip()


def collect_existing(summary_text: str):
    links = set()
    for line in summary_text.splitlines():
        if "](" not in line:
            continue
        rest = line.split("](", 1)[1]
        target = rest.split(")", 1)[0].strip("<>")
        if target:
            links.add(target)
    return links


def main():
    if not SUMMARY.exists():
        raise FileNotFoundError(f"{SUMMARY} not found")

    summary_text = SUMMARY.read_text(encoding="utf-8")
    existing = collect_existing(summary_text)

    missing = []
    for path in sorted(SRC.rglob("*.md")):
        rel = path.relative_to(SRC).as_posix()
        if rel in EXCLUDED or rel in existing:
            continue
        missing.append(rel)

    if not missing:
        print("No missing markdown files detected. SUMMARY.md is up to date.")
        return

    lines = []
    for rel in sorted(missing):
        title = clean_title(Path(rel).name)
        lines.append(f"- [{title}]({rel})")

    summary_text = summary_text.rstrip() + "\n\n" + "\n".join(lines) + "\n"
    SUMMARY.write_text(summary_text, encoding="utf-8")

    print("Added missing entries:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()