#!/usr/bin/env python3

import re
import json
import sys
from pathlib import Path

IDEA_SIGNATURE_RE = re.compile(r'/\*\s*@idea:(small|big|huge)\s+(.+?)\s*\*/', re.UNICODE)
FILE_RE = re.compile(r'([./\w\-]+?\.(c|h|rs|cpp|txt|md))', re.UNICODE)
FUNC_REF_RE = re.compile(r'`([a-zA-Z_][a-zA-Z0-9_]*)\(\)`', re.UNICODE)
IGNORED_KEYWORDS = {"if", "for", "while", "switch", "return", "sizeof"}

def extract_ideas_from_file(path):
    ideas = []

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    full_text = "".join(lines)
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        m = IDEA_SIGNATURE_RE.match(line)
        if m:
            size, name = m.groups()
            start_idx = idx + 1
            content_lines = []

            while start_idx < len(lines):
                l = lines[start_idx].rstrip()
                content_lines.append(l)
                if l.strip().endswith("*/"):
                    start_idx += 1
                    break
                start_idx += 1

            raw_text = "\n".join(content_lines)
            md_text = clean_comment_markers(raw_text)

            remaining_text = "\n".join(lines[start_idx:])

            refs = extract_refs(md_text, remaining_text)
            refs["bugs"] = extract_bugs(md_text)

            ideas.append({
                "path": str(path),
                "name": name.strip(),
                "size": size,
                "start_line": idx + 1,
                "end_line": start_idx,
                "raw_text": raw_text,
                "content_md": md_text,
                "references": refs
            })

            idx = start_idx
        else:
            idx += 1

    return ideas


def clean_comment_markers(raw: str) -> str:
    lines = raw.splitlines()
    cleaned = []
    in_code_block = False

    for l in lines:
        stripped = l.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            cleaned.append(stripped)
            continue

        if in_code_block:
            cleaned.append(l)
            continue

        line = l
        if line.lstrip().startswith("/*") or line.lstrip().startswith("*") or line.lstrip().startswith("//"):
            line = re.sub(r'^(\s*/\*+|\s*\*+|\s*//+)\s?', '', line)

        line = re.sub(r'\*/\s*$', '', line).rstrip()

        md_header_match = re.match(r'^(\s*#{1,6})\s*(.+?):\s*(.*)$', line)
        if md_header_match:
            hashes, title, rest = md_header_match.groups()
            cleaned.append(f"{hashes} {title}")
            if rest:
                cleaned.append(rest)
        else:
            cleaned.append(line)

    return "\n".join(cleaned)


def extract_refs(md_text: str, code_text: str):
    import re

    combined_text = md_text + "\n" + code_text
    lines = combined_text.splitlines()

    char_to_line = []
    offset = 0
    for i, line in enumerate(lines, 1):
        for _ in line:
            char_to_line.append(i)
        char_to_line.append(i)
        offset += len(line) + 1

    functions = []
    FUNC_REF_RE = re.compile(r'`([a-zA-Z_][a-zA-Z0-9_]*)\(\)`')
    for match in FUNC_REF_RE.finditer(combined_text):
        name = match.group(1)
        if name not in IGNORED_KEYWORDS:
            start_idx = match.start()
            line_number = char_to_line[start_idx] if start_idx < len(char_to_line) else 1
            functions.append({
                "name": name,
                "start_idx": start_idx,
                "end_idx": match.end(),
                "line": line_number
            })

    FILE_RE = re.compile(r'([./\w\-]+?\.(c|h|rs|cpp|txt|md))')
    files = []
    for match in FILE_RE.finditer(combined_text):
        files.append({
            "name": match.group(1),
            "start_idx": match.start(),
            "end_idx": match.end()
        })

    return {"functions": functions, "files": files}

def write_ideas_to_json(ideas, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(ideas, f, indent=2, ensure_ascii=False)

def extract_bugs(md_text: str):
    bugs = []
    lines = md_text.splitlines()
    in_bugs_section = False
    offset = 0 

    for line in lines:
        stripped = line.strip()

        if re.match(r'^#{1,6}\s*Bugs', stripped):
            in_bugs_section = True
            offset += len(line) + 1
            continue

        if in_bugs_section and re.match(r'^#{1,6}\s*\w+', stripped):
            in_bugs_section = False

        if in_bugs_section:
            for match in re.finditer(r'#(\d+)', line):
                bugs.append({
                    "start_idx": offset + match.start(),
                    "end_idx": offset + match.end(),
                    "number": int(match.group(1))
                })

        offset += len(line) + 1 

    return bugs


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_json>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_json = Path(sys.argv[2])

    if not input_file.is_file():
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit(1)

    ideas = extract_ideas_from_file(input_file)
    write_ideas_to_json(ideas, output_json)
    print(f"Processed {input_file}, found {len(ideas)} ideas.")
    print(f"Output written to {output_json}")

if __name__ == "__main__":
    main()

