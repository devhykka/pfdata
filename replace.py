#!/usr/bin/env python3

import os
import sys

OLD = "INITIAL CLIMB AS CHARTED"
NEW = "Pilot briefings at wiki.pfatc.net"

search_dir = sys.argv[1] if len(sys.argv) > 1 else "."

print(f"Searching in: {os.path.abspath(search_dir)}")
print(f"Replacing:    {OLD}")
print(f"With:         {NEW}")
print()

matched_files = []

for root, dirs, files in os.walk(search_dir):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for filename in files:
        filepath = os.path.join(root, filename)
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            if OLD in content:
                matched_files.append((filepath, content))
        except Exception:
            pass

if not matched_files:
    print(f"No files found containing '{OLD}'")
    sys.exit(0)

print(f"Found {len(matched_files)} file(s):")
for filepath, _ in matched_files:
    print(f"  {filepath}")
print()

confirm = input("Proceed with replacement? (y/n): ").strip().lower()
if confirm != "y":
    print("Aborted.")
    sys.exit(0)

print()
total_replacements = 0
for filepath, content in matched_files:
    count = content.count(OLD)
    new_content = content.replace(OLD, NEW)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {filepath} ({count} replacement(s))")
    total_replacements += count

print()
print(f"Done. {len(matched_files)} file(s) updated, {total_replacements} replacement(s) made.")