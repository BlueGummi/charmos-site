#!/usr/bin/env python3
import json
import sys
import re
from pathlib import Path
from collections import defaultdict

SOURCE_REPO_URL = "https://github.com/bluegummi/charmos/blob/main"
BUG_URL_BASE = "https://github.com/bluegummi/charmos/issues"
DOCS_ROOT = Path("./docs")
IGNORED_KEYWORDS = {"if", "for", "while", "switch", "return", "sizeof"}

def load_json_dir(json_dir: Path):
    ideas = []
    for path in json_dir.glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            ideas.extend(json.load(f))
    return ideas

def make_docs_path(idea_path: str, idea_name: str, big_or_small="big", collision_count=0):
    src_path = Path(idea_path)
    base = src_path.stem
    if big_or_small == "small":
        md_name = "root"
        if collision_count > 0:
            md_name += f"-{collision_count}"
    else:
        md_name = base
        if collision_count > 0:
            md_name += f"-{collision_count}"
    doc_dir = DOCS_ROOT / src_path.parent
    doc_dir.mkdir(parents=True, exist_ok=True)
    return doc_dir / f"{md_name}.md"

def generate_github_link(file_path: str, line: int = None):
    url = f"{SOURCE_REPO_URL}/{file_path}"
    if line:
        url += f"#L{line}"
    return url

def link_functions_in_md(md_text: str, functions_map: dict):
    FUNC_RE = re.compile(r'`([a-zA-Z_][a-zA-Z0-9_]*)\(\)`')
    def replacer(match):
        fn = match.group(1)
        url = functions_map.get(fn)
        if url:
            return f"[`{fn}()`]({url})"
        return match.group(0)
    return FUNC_RE.sub(replacer, md_text)

def link_files_in_md(md_text: str, files_map: dict):
    FILE_RE = re.compile(r'`([\w./-]+\.(c|h|rs|cpp|txt|md))`')
    def replacer(match):
        file = match.group(1)
        url = files_map.get(file)
        if url:
            return f"[`{file}`]({url})"
        return match.group(0)
    return FILE_RE.sub(replacer, md_text)

def link_bugs_in_md(md_text: str):
    BUG_RE = re.compile(r'#(\d+)')
    def replacer(match):
        bug_number = match.group(1)
        url = f"{BUG_URL_BASE}/{bug_number}"
        return f"[#{bug_number}]({url})"
    return BUG_RE.sub(replacer, md_text)



def extract_mdx_title(md_text: str):
    lines = md_text.splitlines()
    cleaned_lines = []
    idea_type = None
    idea_name = None
    credits = None

    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()

        m = re.match(r'^#\s*(Big|Small|Huge)\s+Idea\s*:\s*(.+)$', line, re.IGNORECASE)
        if m:
            idea_type, idea_name = m.groups()
            idx += 1
            continue

        m2 = re.match(r'^#\s*(Big|Small|Huge)\s+Idea\s*$', line, re.IGNORECASE)
        if m2 and idx + 1 < len(lines):
            idea_type = m2.group(1)
            next_line = lines[idx + 1].strip()
            if next_line:
                idea_name = next_line
                idx += 2
                continue

        if re.match(r'^#\s*Credits\s*$', line, re.IGNORECASE) and idx + 1 < len(lines):
            credits_line = lines[idx + 1].strip()
            if credits_line:
                credits = credits_line
                idx += 2
                # If the next line is blank, skip it too to prevent double newline
                if idx < len(lines) and lines[idx].strip() == "":
                    idx += 1
                continue

        cleaned_lines.append(lines[idx])
        idx += 1

    if not idea_type or not idea_name:
        idea_type = "Idea"
        idea_name = "Untitled"

    mdx_title_lines = [f"# {idea_type.capitalize()} Idea: {idea_name}"]
    if credits:
        mdx_title_lines.append(f"**Credits:** {credits}")

    mdx_title = "\n".join(mdx_title_lines)
    cleaned_body = "\n".join(cleaned_lines).strip()
    return mdx_title, cleaned_body



def generate_docs(json_dir: Path):
    ideas = load_json_dir(json_dir)

    functions_map = {}
    files_map = {}

    for idea in ideas:
        for fn in idea.get("references", {}).get("functions", []):
            functions_map[fn["name"]] = generate_github_link(idea["path"], fn.get("line"))
        for f in idea.get("references", {}).get("files", []):
            files_map[f["name"]] = generate_github_link(f["name"])

    collision_counter = defaultdict(int)

    for idea in ideas:
        size = idea["size"]
        idea_path = idea["path"]
        idea_name = idea["name"]
        collision_count = collision_counter[idea_name]
        md_path = make_docs_path(
            idea_path, idea_name, "big" if size != "small" else "small", collision_count
        )
        collision_counter[idea_name] += 1

        md_text = idea["content_md"]

        mdx_title, md_body = extract_mdx_title(md_text)

        md_body = link_functions_in_md(md_body, functions_map)
        md_body = link_files_in_md(md_body, files_map)
        md_body = link_bugs_in_md(md_body)

        if idea.get("references", {}).get("functions"):
            md_body += "\n\n## Functions\n"
            for fn in idea["references"]["functions"]:
                url = functions_map.get(fn["name"])
                if url:
                    md_body += f"- [`{fn['name']}()`]({url})\n"

        md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"{mdx_title}\n\n{md_body}")

        print(f"Wrote {md_path}")



def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <json_dir>")
        sys.exit(1)

    json_dir = Path(sys.argv[1])
    if not json_dir.is_dir():
        print(f"Error: {json_dir} is not a directory")
        sys.exit(1)

    generate_docs(json_dir)

if __name__ == "__main__":
    main()

