#!/usr/bin/env python3
import json
import sys
import re, shutil
from pathlib import Path
from collections import defaultdict

SOURCE_REPO_URL = "https://github.com/bluegummi/charmos/blob/main"
BUG_URL_BASE = "https://github.com/bluegummi/charmos/issues"
DOCS_ROOT = Path("./docs")

IGNORED_KEYWORDS = {"if", "for", "while", "switch", "return", "sizeof"}

def print_single_line(*args, progress: float = None, **kwargs):
    text = " ".join(str(arg) for arg in args)
    terminal_width = shutil.get_terminal_size((80, 20)).columns

    if progress is not None:
        progress_str = f"{int(progress * 100)}%"
        space_to_progress = max(terminal_width - len(text) - len(progress_str), 1)
        output = "\r" + text + " " * space_to_progress + progress_str
    else:
        spaces_to_clear = max(terminal_width - len(text), 0)
        output = "\r" + text + " " * spaces_to_clear

    flush = kwargs.get("flush", True)
    sys.stdout.write(output)
    if flush:
        sys.stdout.flush()

def make_docs_path(idea_path: str, md_root: Path = DOCS_ROOT) -> Path:
    src_path = Path(idea_path)
    try:
        relative_path = src_path.relative_to("charmos/include")
    except ValueError:
        relative_path = src_path

    md_file = relative_path.with_suffix(".mdx").name  
    md_path = md_root / md_file
    md_path.parent.mkdir(parents=True, exist_ok=True)
    return md_path


def normalize_type_name(type_str: str) -> str:
    type_str = type_str.strip()
    type_str = re.sub(r'\bconst\b', '', type_str)
    type_str = type_str.replace('*', '')
    type_str = re.sub(r'\s+', ' ', type_str)
    type_str = type_str.replace('[]', '')
    return type_str.strip().lower()

def link_type(type_str: str, type_table: dict, always_tick) -> str:
    norm = normalize_type_name(type_str)
    entry = type_table.get(norm)
    if not entry:
        if always_tick:
            return f"`{type_str}`"
        else:
            return f" {type_str} " 

    url = generate_github_link_safe(entry["file"], entry["line"])
    return f"[`{type_str}`]({url})"


def build_type_table(c_parse_map: dict, ignored_types=None):
    if ignored_types is None:
        ignored_types = set()

    type_table = {}

    for file_path, c_parse in c_parse_map.items():
        types = c_parse.get("types", {})

        # Structs
        for s in types.get("structs", []):
            name = s.get("name")
            if not name or name in ignored_types:
                continue
            full_name = f"struct {name}"
            type_table[full_name.lower()] = {
                "name": name,
                "full_name": full_name,
                "file": file_path,
                "line": s.get("line"),
                "start_byte": s.get("start_byte"),
                "end_byte": s.get("end_byte"),
                "kind": "struct"
            }

        # Enums
        for e in types.get("enums", []):
            name = e.get("name")
            if not name or name in ignored_types:
                continue
            full_name = f"enum {name}"
            type_table[full_name.lower()] = {
                "name": name,
                "full_name": full_name,
                "file": file_path,
                "line": e.get("line"),
                "start_byte": e.get("start_byte"),
                "end_byte": e.get("end_byte"),
                "kind": "enum"
            }

        # Typedefs
        for t in types.get("typedefs", []):
            name = t.get("name")
            if not name or name in ignored_types:
                continue
            full_name = name
            type_table[full_name.lower()] = {
                "name": name,
                "full_name": full_name,
                "file": file_path,
                "line": t.get("line"),
                "start_byte": t.get("start_byte"),
                "end_byte": t.get("end_byte"),
                "kind": "typedef",
                "type_str": t.get("type")
            }

    return type_table


def generate_github_link_safe(file_path: str, line: int = None) -> str:
    src_path = Path(file_path)
    try:
        relative_path = src_path.relative_to("charmos")
    except ValueError:
        relative_path = src_path

    url = f"{SOURCE_REPO_URL}/{relative_path.as_posix()}"
    if line is not None:
        url += f"#L{line}"

    url = re.sub(r"/blob/main/charmos/", "/blob/main/", url)
    return url

def load_json_dir(json_dir: Path):
    all_ideas = []
    c_parse_map = {}
    for path in json_dir.glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            ideas = data.get("ideas", [])
            all_ideas.extend(ideas)
            c_parse_map[data.get("file")] = data.get("c_parse", {})
    return all_ideas, c_parse_map

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

def link_commits_in_md(md_text: str):
    COMMIT_RE = re.compile(r'commit\s+([0-9a-f]{7,40})', re.IGNORECASE)
    def replacer(match):
        h = match.group(1)
        url = f"https://github.com/bluegummi/charmos/commit/{h}"
        return f"[commit {h}]({url})"
    return COMMIT_RE.sub(replacer, md_text)

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

def embed_idea_refs_in_md(md_text: str, idea, idea_doc_paths):
    refs = idea.get("references", {}).get("idea_refs", [])
    if not refs:
        return md_text

    for ref in refs:
        ref_string = ref["string"]
        ref_lower = ref_string.lower()

        target_path = None
        for name, path in idea_doc_paths.items():
            if ref_lower in name:
                target_path = path
                break

        if not target_path:
            continue

        link_url = generate_github_link_safe(target_path)
        link_md = f"[`{target_path.name}`]({link_url})"
        pattern = re.escape(ref_string)
        md_text = re.sub(pattern, f'"{ref_string}" {link_md}', md_text)

    return md_text

def generate_docs(json_dir: Path):
    ideas, c_parse_map = load_json_dir(json_dir)
    type_table = build_type_table(c_parse_map)

    # Step 1: Group ideas by their source file

    functions_map = {}
    files_map = {}
    idea_doc_paths = {}
    ideas_by_file = defaultdict(list)
    collision_counter = defaultdict(int)
    json_files = list(json_dir.glob("*.json")) 
    total_files = len(json_files)

    for idea in ideas:
        src_file = idea["path"]
        ideas_by_file[src_file].append(idea)
    
    # Second pass: build function/file links
    for idea in ideas:
        for fn in idea.get("references", {}).get("functions", []):
            functions_map[fn["name"]] = generate_github_link_safe(idea["path"], fn.get("line"))

        for f in idea.get("references", {}).get("files", []):
            files_map[f["name"]] = generate_github_link_safe(f["name"])

    # Step 2: For each JSON file, write the Markdown with ideas on top
    for i, json_file in enumerate(json_dir.glob("*.json"), start = 1):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    
        source_path = Path(data["file"])
        try:
            relative_path = source_path.relative_to("charmos/include")
        except ValueError:
            relative_path = source_path
    
        md_out_path = DOCS_ROOT / relative_path.parent / (relative_path.stem + ".mdx")
        md_out_path.parent.mkdir(parents=True, exist_ok=True)
    
        # Gather ideas for this file
        file_ideas = ideas_by_file.get(str(source_path), [])
        
        if file_ideas:
            first_idea = file_ideas[0]
            title = first_idea.get("name", md_out_path.stem)
            author = first_idea.get("author", "Unknown")
            status = first_idea.get("status", "unknown")
        else:
            title = md_out_path.stem
            author = "Unknown"
            status = "unknown"
                
        front_matter_lines = [
            "---\n",
            f'title: "{title}"\n',
            f'author: "{author}"\n', 
            f'status: "{status}"\n',
            "---\n\n"
        ]

        
            
                # Build the combined Markdown
        combined_lines = []
    
        for idea in file_ideas:
            md_text = idea["content_md"]
            mdx_title, md_body = extract_mdx_title(md_text)
            md_body = link_functions_in_md(md_body, functions_map)
            md_body = link_files_in_md(md_body, files_map)
            md_body = link_bugs_in_md(md_body)
            md_body = link_commits_in_md(md_body)
            md_body = embed_idea_refs_in_md(md_body, idea, idea_doc_paths)
    
            idea_name = idea["name"]
            combined_lines.append(f"# {idea['size'].capitalize()} Idea: {idea_name}\n")
            author = idea.get("author", "Unknown")
            status = idea.get("status", "unknown")
            combined_lines.append(f"**Author:** {author} | **Status:** {status}\n\n")
            combined_lines.append(md_body)
            combined_lines.append("\n---\n")  # separator between ideas
    
        file_md_lines = []
    
        def collect_markdown_lines(json_path, type_table):
            data = json.loads(open(json_path, encoding="utf-8").read())
            lines = []
    
            source_path = Path(data["file"])
            file_url = generate_github_link_safe(data["file"])
            lines.append(f"# [{source_path.as_posix()[8:]}]({file_url})\n")
    
            # Structs
            for s in data["c_parse"]["types"].get("structs", []):
                if not s.get("name") or s["name"].lower() == "none":
                    continue
                struct_url = generate_github_link_safe(data["file"], s.get("line"))
                lines.append(f"### struct [`{s['name']}`]({struct_url})\n")
                if s.get("members"):
                    lines.append("| Member Type | Member Name |")
                    lines.append("|-------------|-------------|")
                    for m in s["members"]:
                        member_url = generate_github_link_safe(data["file"], m.get("line"))
                        member_type_link = link_type(m['type'], type_table, True)
                        member_type_link = clean_string(member_type_link)
                        lines.append(f"| {member_type_link} | [`{m['name']}`]({member_url}) |")
                else:
                    lines.append("_No members_\n")
                lines.append("\n")
    
            # Enums
            for e in data["c_parse"]["types"].get("enums", []):
                if not e.get("name") or e["name"].lower() == "none":
                    continue
                enum_url = generate_github_link_safe(data["file"], e.get("line"))
                lines.append(f"### enum [`{e['name']}`]({enum_url})\n")
                if e.get("members"):
                    lines.append("| Name | Value |")
                    lines.append("|------|-------|")
                    for m in e["members"]:
                        member_url = generate_github_link_safe(data["file"], m.get("line"))
                        lines.append(f"| [`{m['name']}`]({member_url}) | `{m['value']}` |")
                lines.append("\n")
    
            # Typedefs
            for t in data["c_parse"]["types"].get("typedefs", []):
                if not t.get("name"):
                    continue
                t_url = generate_github_link_safe(data["file"], t.get("line"))
                linked_type_str = clean_string(link_type(t['type'], type_table, True))
                lines.append(f"### type alias\n[`{t['name']}`]({t_url}) : {linked_type_str}")
    
            # Functions
            for f in data["c_parse"].get("functions", []):
                if not f.get("name"):
                    continue
                signature_md = format_function_signature(data, f, type_table)
                lines.append(f"- {signature_md}")
    
            if data["c_parse"].get("functions"):
                lines.append("\n")
    
            return lines
    
        file_md_lines = collect_markdown_lines(json_file, type_table)
        combined_lines.extend(file_md_lines)
    
        # Write combined Markdown to single file
        md_out_path.write_text("".join(front_matter_lines) + "\n".join(combined_lines), encoding="utf-8")
        print_single_line("compiled JSON " + str(json_dir) + " → " + str(md_out_path), progress = i / total_files)
    

def format_function_signature_raw(data, f, type_table):
    qualifiers = " ".join(f.get("qualifiers", []))
    return_type = f.get("return_type") or "void"

    parts = []
    if qualifiers:
        parts.append(qualifiers)
    
    ret_type_full = link_type(return_type, type_table, False)
    if not qualifiers:
        ret_type_full = ret_type_full.lstrip()

    parts.append(ret_type_full)

    f_url = generate_github_link_safe(data["file"], f.get("line"))
    parts.append(f"[`{f['name']}`]({f_url})")

    parts.append("(")

    param_strs = []
    for p in f.get("parameters", []):
        type_md = link_type(p['type'], type_table, False).strip()
        if p.get("name"):
            param_strs.append(f"{type_md} {p['name']}")
        else:
            param_strs.append(type_md)
    parts.append(",".join(param_strs))
    parts.append(")")

    return "".join(parts)

def retick_segmentwise(s: str) -> str:
    out = []
    i = 0
    n = len(s)

    out.append("`")  # start the first tick

    while i < n:
        c = s[i]

        # Rule A: hit a link
        if c == "[" and i + 1 < n and s[i + 1] == "`":
            # end current tick
            out.append("`")
            # copy the entire link verbatim
            link_start = i
            # find the closing ')'
            # because markdown link is always [text](url)
            j = s.find(")", i)
            if j == -1:
                # malformed; just treat '[' as normal char
                out.append("`")  # reopen tick
                out.append(c)
                i += 1
                continue
            link_end = j + 1
            out.append(s[link_start:link_end])

            # restart ticking
            out.append("`")
            i = link_end
            continue

        # Rule B: hit a comma
        if c == ",":
            # close tick
            out.append("`")
            out.append(",")
            # restart
            out.append("`")
            i += 1
            continue

        # default case: normal character inside tick
        out.append(c)
        i += 1

    # close final tick
    out.append("`")
    return "".join(out)


def clean_string(input_string):
    cleaned_string = ' '.join(line.lstrip() for line in input_string.splitlines())
    return cleaned_string

def format_function_signature(data, f, type_table):
    raw = format_function_signature_raw(data, f, type_table)
    final = retick_segmentwise(raw)
    final = re.sub('`{2,}', '', final)
    return final


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

