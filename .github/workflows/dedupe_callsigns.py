"""Remove exact duplicate rows from callsigns.json.

A row is an exact duplicate when the same `icao` + `callsign` pair already
appeared earlier in the file. Only those rows are removed (the first
occurrence is kept, file order is otherwise unchanged). ICAO codes with
genuinely conflicting callsign text are left alone — those need a human
decision and are reported by validate_data.py instead.

Used by data-callsigns-autofix.yml and data-validate-nightly.yml.
"""
import argparse
import json
import os
import sys


def dedupe(entries):
    seen = set()
    kept = []
    removed = 0
    for entry in entries:
        if isinstance(entry, dict):
            key = (entry.get("icao"), entry.get("callsign"))
            if key in seen:
                removed += 1
                continue
            seen.add(key)
        kept.append(entry)
    return kept, removed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    path = os.path.join(os.path.abspath(args.repo_root), "callsigns.json")
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    if not isinstance(data, list):
        print(f"{path}: expected a JSON array, leaving it untouched.", file=sys.stderr)
        return 1

    kept, removed = dedupe(data)
    if not removed:
        print("No exact duplicate callsign rows found.")
        return 0

    # Match the existing file format (2-space indent, raw UTF-8, trailing newline)
    # so the resulting diff only shows the removed rows.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(kept, indent=2, ensure_ascii=False) + "\n")

    print(f"Removed {removed} exact duplicate row(s) from callsigns.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
