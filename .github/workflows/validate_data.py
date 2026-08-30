#!/usr/bin/env python3
"""
validate_data.py — duplicate & error checker for the pfdata repository.

Scans every source file that feeds the concatenate_*.py build scripts
(.data/runways, .data/sectors, .data/stations, .data/waypoints if present,
plus the hand-edited waypoints.json and callsigns.json) and reports:

  ERROR   — will break the build or silently corrupt output (JSON syntax
            errors, duplicate keys inside one JSON object, duplicate
            filenames across sub-folders that the build scripts key by
            filename stem, duplicate waypoint names, missing/mistyped
            required fields, duplicate station callsigns).
  WARNING — worth a human look but not build-breaking (duplicate ICAO
            codes / callsign text in callsigns.json — there's a large
            pre-existing backlog of these and ICAO reuse across regions
            is sometimes legitimate).

Exit code is 1 if any ERROR-level issue is found, 0 otherwise. Warnings
never fail the build.

Usage:
    python validate_data.py [--repo-root .] [--json report.json] [--markdown report.md]
"""

import argparse
import glob
import json
import os
import sys
from collections import defaultdict

ERROR = "error"
WARNING = "warning"


class Report:
    def __init__(self):
        self.issues = []  # list of dicts: severity, category, file, message, detail, row

    def add(self, severity, category, file, message, detail=None, row=None):
        """`message` is the short, single-line form used in GitHub Actions
        annotations and the job log. `detail`, if given, is a longer
        (optionally markdown/HTML) block used instead of `message` in the
        PR-comment / issue report. `row`, if given, is a list of column
        values — when every issue in a category has one, build_markdown()
        renders that whole category as a single sortable table instead of
        a bullet per issue, which is far more readable for anything with
        more than a couple of findings."""
        self.issues.append({
            "severity": severity,
            "category": category,
            "file": file,
            "message": message,
            "detail": detail,
            "row": row,
        })

    def errors(self):
        return [i for i in self.issues if i["severity"] == ERROR]

    def warnings(self):
        return [i for i in self.issues if i["severity"] == WARNING]


# Column headers for categories that report structured `row` data. Any
# category not listed here (or where an issue is missing its `row`) falls
# back to a plain bullet list using `message`.
TABLE_HEADERS = {
    "duplicate-filename": ["Filename stem", "Colliding files"],
    "duplicate-waypoint": ["Waypoint", "Occurrences"],
    "overlapping-coords": ["Coordinates", "Waypoints sharing them"],
    "duplicate-callsign": ["Callsign", "Files"],
    "duplicate-name": ["Sector name", "Files"],
    "duplicate-icao-exact": ["ICAO", "Callsign", "Repeated ×"],
    "duplicate-icao-conflict": ["ICAO", "Conflicting callsign entries"],
}


def _dup_key_hook(pairs):
    """object_pairs_hook that records duplicate keys but still returns a usable dict."""
    seen = {}
    dupes = []
    for k, v in pairs:
        if k in seen:
            dupes.append(k)
        seen[k] = v
    if dupes:
        seen["__duplicate_keys__"] = sorted(set(dupes))
    return seen


def load_json_checked(path, report):
    """Load JSON, flagging syntax errors and duplicate object keys anywhere in the file."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        report.add(ERROR, "read", path, f"Could not read file: {exc}")
        return None

    try:
        data = json.loads(text, object_pairs_hook=_dup_key_hook)
    except json.JSONDecodeError as exc:
        report.add(ERROR, "syntax", path,
                    f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return None

    def scan_for_dupe_marker(obj, ctx=""):
        if isinstance(obj, dict):
            dupes = obj.get("__duplicate_keys__")
            if dupes:
                report.add(ERROR, "duplicate-key", path,
                            f"Duplicate JSON key(s) {dupes} in object{(' at ' + ctx) if ctx else ''} "
                            f"— the later value silently overwrote the earlier one.")
            for k, v in obj.items():
                if k == "__duplicate_keys__":
                    continue
                scan_for_dupe_marker(v, f"{ctx}.{k}" if ctx else k)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                scan_for_dupe_marker(item, f"{ctx}[{idx}]")

    scan_for_dupe_marker(data)
    return data


def find_duplicate_filenames(source_dir, report, repo_root, case_insensitive=True):
    """Flag filename stems that repeat anywhere under source_dir (across sub-folders).

    The build scripts key their output dict purely by `os.path.splitext(filename)[0]`,
    so two files with the same stem in different sub-folders silently overwrite one
    another with no error — whichever os.walk() visits last wins, non-deterministically.
    """
    stems = defaultdict(list)
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if not filename.lower().endswith(".json"):
                continue
            stem = os.path.splitext(filename)[0]
            key = stem.lower() if case_insensitive else stem
            stems[key].append(os.path.relpath(os.path.join(dirpath, filename), repo_root))

    for key, paths in stems.items():
        if len(paths) > 1:
            report.add(
                ERROR, "duplicate-filename", source_dir,
                f"Filename stem '{key}' appears in {len(paths)} files — the build script "
                f"keys its output by filename only, so these silently collide: "
                f"{', '.join(sorted(paths))}",
                row=[f"`{key}`", ", ".join(f"`{p}`" for p in sorted(paths))],
            )


def validate_runways(repo_root, report):
    source_dir = os.path.join(repo_root, ".data", "runways")
    if not os.path.isdir(source_dir):
        return
    find_duplicate_filenames(source_dir, report, repo_root)

    for path in sorted(glob.glob(os.path.join(source_dir, "*.json"))):
        data = load_json_checked(path, report)
        if data is None:
            continue
        if not isinstance(data, dict):
            report.add(ERROR, "schema", path, "Expected a JSON object of {runway: [freq, x, heading]}.")
            continue
        for ident, value in data.items():
            if ident == "__duplicate_keys__":
                continue
            if not isinstance(value, list) or len(value) != 3:
                report.add(ERROR, "schema", path,
                            f"Runway '{ident}' should be a 3-element array [freq, x, heading], got: {value!r}")
                continue
            for v in value:
                try:
                    float(v)
                except (TypeError, ValueError):
                    report.add(ERROR, "schema", path,
                                f"Runway '{ident}' has a non-numeric value: {v!r}")


def validate_sectors(repo_root, report):
    source_dir = os.path.join(repo_root, ".data", "sectors")
    if not os.path.isdir(source_dir):
        return
    find_duplicate_filenames(source_dir, report, repo_root)

    names_seen = defaultdict(list)
    for path in sorted(glob.glob(os.path.join(source_dir, "**", "*.json"), recursive=True)):
        data = load_json_checked(path, report)
        if data is None:
            continue
        if not isinstance(data, dict):
            report.add(ERROR, "schema", path, "Expected a JSON object with 'name' and 'topdown' keys.")
            continue
        if "name" not in data or not isinstance(data.get("name"), str) or not data["name"].strip():
            report.add(ERROR, "schema", path, "Missing or empty required field 'name'.")
        if "topdown" not in data or not isinstance(data.get("topdown"), list):
            report.add(ERROR, "schema", path, "Missing or invalid required field 'topdown' (expected a list).")
        if data.get("name"):
            names_seen[data["name"]].append(os.path.relpath(path, repo_root))

    for name, paths in names_seen.items():
        if len(paths) > 1:
            report.add(WARNING, "duplicate-name", source_dir,
                        f"Sector name '{name}' is used in {len(paths)} files: {', '.join(paths)}",
                        row=[name, ", ".join(f"`{p}`" for p in paths)])


def validate_stations(repo_root, report):
    source_dir = os.path.join(repo_root, ".data", "stations")
    if not os.path.isdir(source_dir):
        return
    find_duplicate_filenames(source_dir, report, repo_root)

    callsigns_seen = defaultdict(list)
    required_fields = ("name", "callsign", "frequency", "facility")

    for path in sorted(glob.glob(os.path.join(source_dir, "**", "*.json"), recursive=True)):
        data = load_json_checked(path, report)
        if data is None:
            continue
        # Source files may be a single station object or a list of them.
        stations = data if isinstance(data, list) else [data]

        for idx, station in enumerate(stations):
            if not isinstance(station, dict):
                report.add(ERROR, "schema", path, f"Entry {idx} is not a JSON object.")
                continue
            for field in required_fields:
                if field not in station:
                    report.add(ERROR, "schema", path,
                                f"Entry {idx} ('{station.get('name', '?')}') is missing required field '{field}'.")
            if "frequency" in station and not isinstance(station["frequency"], (int, float)):
                report.add(ERROR, "schema", path,
                            f"Entry {idx} ('{station.get('name', '?')}') has a non-numeric frequency: "
                            f"{station['frequency']!r}")
            callsign = station.get("callsign")
            if isinstance(callsign, str) and callsign:
                callsigns_seen[callsign].append(os.path.relpath(path, repo_root))

    for callsign, paths in callsigns_seen.items():
        if len(paths) > 1:
            unique_paths = sorted(set(paths))
            report.add(ERROR, "duplicate-callsign", source_dir,
                        f"Callsign '{callsign}' is used {len(paths)} times "
                        f"across {len(unique_paths)} file(s): {', '.join(unique_paths)}",
                        row=[f"`{callsign}`", ", ".join(f"`{p}`" for p in unique_paths)])


def validate_waypoints(repo_root, report):
    candidates = [os.path.join(repo_root, "waypoints.json")]
    data_dir = os.path.join(repo_root, ".data", "waypoints")
    if os.path.isdir(data_dir):
        find_duplicate_filenames(data_dir, report, repo_root)
        candidates.extend(sorted(glob.glob(os.path.join(data_dir, "**", "*.json"), recursive=True)))

    names_seen = defaultdict(list)
    coords_seen = defaultdict(list)

    for path in candidates:
        if not os.path.isfile(path):
            continue
        data = load_json_checked(path, report)
        if data is None:
            continue
        if not isinstance(data, list):
            report.add(ERROR, "schema", path, "Expected a JSON array of waypoint objects.")
            continue
        for idx, wp in enumerate(data):
            if not isinstance(wp, dict):
                report.add(ERROR, "schema", path, f"Entry {idx} is not a JSON object.")
                continue
            for field in ("name", "x", "y", "type"):
                if field not in wp:
                    report.add(ERROR, "schema", path,
                                f"Entry {idx} ('{wp.get('name', '?')}') is missing required field '{field}'.")
            if not isinstance(wp.get("x"), (int, float)) or not isinstance(wp.get("y"), (int, float)):
                report.add(ERROR, "schema", path,
                            f"Entry {idx} ('{wp.get('name', '?')}') has non-numeric x/y.")
            name = wp.get("name")
            if isinstance(name, str) and name:
                rel_path = os.path.relpath(path, repo_root)
                names_seen[name].append((rel_path, wp.get("x"), wp.get("y")))
                coords_seen[(wp.get("x"), wp.get("y"))].append(name)

    for name, occurrences in names_seen.items():
        if len(occurrences) > 1:
            locs = "; ".join(f"{p} @ ({x}, {y})" for p, x, y in occurrences)
            report.add(ERROR, "duplicate-waypoint", "waypoints",
                        f"Waypoint name '{name}' is defined {len(occurrences)} times: {locs}",
                        row=[f"`{name}`", "<br>".join(f"`{p}` @ ({x}, {y})" for p, x, y in occurrences)])

    for (x, y), names in coords_seen.items():
        unique_names = sorted(set(names))
        if len(unique_names) > 1:
            report.add(WARNING, "overlapping-coords", "waypoints",
                        f"Waypoints {unique_names} share the exact same coordinates ({x}, {y}).",
                        row=[f"({x}, {y})", ", ".join(f"`{n}`" for n in unique_names)])


def validate_callsigns(repo_root, report):
    path = os.path.join(repo_root, "callsigns.json")
    if not os.path.isfile(path):
        return
    data = load_json_checked(path, report)
    if data is None:
        return
    if not isinstance(data, list):
        report.add(ERROR, "schema", path, "Expected a JSON array of {icao, callsign} objects.")
        return

    icao_seen = defaultdict(list)
    for idx, entry in enumerate(data):
        if not isinstance(entry, dict) or "icao" not in entry or "callsign" not in entry:
            report.add(ERROR, "schema", path, f"Entry {idx} is missing 'icao' or 'callsign'.")
            continue
        icao_seen[entry["icao"]].append(entry["callsign"])

    # "exact" = every entry for that ICAO has the identical callsign text —
    # a plain redundant copy, safe to auto-remove (see dedupe_callsigns.py).
    # "conflicting" = different callsign text competing for the same ICAO —
    # needs a human to pick the right one; ICAO reuse across regions can be
    # legitimate, so this is never auto-fixed.
    for icao, callsigns in sorted(icao_seen.items()):
        if len(callsigns) < 2:
            continue
        distinct = sorted(set(callsigns))
        if len(distinct) == 1:
            report.add(WARNING, "duplicate-icao-exact", path,
                        f"ICAO '{icao}' repeats \"{distinct[0]}\" {len(callsigns)}×.",
                        row=[f"`{icao}`", distinct[0], str(len(callsigns))])
        else:
            report.add(WARNING, "duplicate-icao-conflict", path,
                        f"ICAO '{icao}' has conflicting entries: {distinct}",
                        row=[f"`{icao}`", " vs ".join(f"\"{c}\"" for c in distinct)])


def _render_category_group(category, issues, repo_root):
    headers = TABLE_HEADERS.get(category)
    has_rows = headers and all(i.get("row") for i in issues)

    if has_rows:
        table_lines = ["| " + " | ".join(headers) + " |",
                       "|" + "|".join(["---"] * len(headers)) + "|"]
        for i in issues:
            cells = [str(c).replace("\n", " ") for c in i["row"]]
            table_lines.append("| " + " | ".join(cells) + " |")
        table = "\n".join(table_lines)

        title = f"{category} — {len(issues)} finding(s)"
        if len(issues) > 6:
            return f"<details><summary>{title}</summary>\n\n{table}\n\n</details>"
        return f"**{title}**\n\n{table}"

    # Fall back to one bullet per issue when there's no structured row data.
    lines = [f"**{category}**"]
    for i in issues:
        rel = os.path.relpath(i["file"], repo_root) if os.path.isabs(i["file"]) else i["file"]
        lines.append(f"- **`{rel}`**: {i['message']}")
        if i.get("detail"):
            lines.append(i["detail"])
    return "\n".join(lines)


def _group_by_category(issues):
    grouped = {}
    for i in issues:
        grouped.setdefault(i["category"], []).append(i)
    return grouped


def build_markdown(report, repo_root):
    errors = report.errors()
    warnings = report.warnings()
    lines = []
    if not errors and not warnings:
        lines.append("✅ **Data validation passed** — no duplicates or errors found.")
        return "\n".join(lines)

    if errors:
        lines.append(f"### ❌ {len(errors)} error(s) — must fix before merge")
        lines.append("")
        for category, group in _group_by_category(errors).items():
            lines.append(_render_category_group(category, group, repo_root))
            lines.append("")

    if warnings:
        lines.append(f"### ⚠️ {len(warnings)} warning(s) — non-blocking, worth a look")
        lines.append("")
        for category, group in _group_by_category(warnings).items():
            lines.append(_render_category_group(category, group, repo_root))
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--json", default="validation-report.json")
    parser.add_argument("--markdown", default="validation-report.md")
    args = parser.parse_args()

    repo_root = os.path.abspath(args.repo_root)
    report = Report()

    validate_runways(repo_root, report)
    validate_sectors(repo_root, report)
    validate_stations(repo_root, report)
    validate_waypoints(repo_root, report)
    validate_callsigns(repo_root, report)

    for i in report.issues:
        rel = os.path.relpath(i["file"], repo_root) if os.path.isabs(i["file"]) else i["file"]
        gh_level = "error" if i["severity"] == ERROR else "warning"
        print(f"::{gh_level} file={rel}::[{i['category']}] {i['message']}")

    with open(args.json, "w", encoding="utf-8") as fh:
        json.dump({
            "errorCount": len(report.errors()),
            "warningCount": len(report.warnings()),
            "issues": report.issues,
        }, fh, indent=2)

    with open(args.markdown, "w", encoding="utf-8") as fh:
        fh.write(build_markdown(report, repo_root))

    print(f"\n{len(report.errors())} error(s), {len(report.warnings())} warning(s).")
    return 1 if report.errors() else 0


if __name__ == "__main__":
    sys.exit(main())
