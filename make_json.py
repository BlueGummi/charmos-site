#!/usr/bin/env python3

import re
import json
import sys, shutil
from pathlib import Path
import tempfile
import subprocess
from tree_sitter import Language, Parser
from pathlib import Path
from tree_sitter_language_pack import get_parser
from tree_sitter import Parser

FILE_TITLE_RE = re.compile(
    r'/\*\s*@title:\s*(.+?)\s*\*/',
    re.IGNORECASE | re.DOTALL
)

IDEA_REF_RE = re.compile(r'\]:\s*"([^"]+)"')
IDEA_SIGNATURE_RE = re.compile(r'/\*\s*@idea:(small|big|huge)\s+(.+?)\s*\*/', re.UNICODE)
FILE_RE = re.compile(r'([./\w\-]+?\.(c|h|rs|cpp|txt|md))', re.UNICODE)
FUNC_REF_RE = re.compile(r'`([a-zA-Z_][a-zA-Z0-9_]*)\(\)`', re.UNICODE)
IGNORED_KEYWORDS = {"if", "for", "while", "switch", "return", "sizeof"}
COMMIT_RE = re.compile(r'(?:\*?\s*)commit\s+([0-9a-f]{7,40})', re.IGNORECASE)

IGNORE_DIRS = ['uACPI', 'flanterm']

parser = get_parser("c")

def extract_file_title(text: str):
    m = FILE_TITLE_RE.search(text)
    if not m:
        return None

    title = m.group(1).strip()

    title = re.sub(r'^\*\s*', '', title).strip()

    return title


def print_single_line(*args, **kwargs):
    text = " ".join(str(arg) for arg in args)
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    spaces_to_clear = max(terminal_width - len(text), 0)
    output = "\r" + text + " " * spaces_to_clear

    flush = kwargs.get("flush", True)

    sys.stdout.write(output)
    if flush:
        sys.stdout.flush()


def extract_metadata(md_text: str):
    name = None
    status = None
    author = None

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if re.match(r'^[#/*\s]*(Big|Huge|Small)\s+Idea', line, re.IGNORECASE):
            if i + 1 < len(lines):
                next_line = re.sub(r'^[#/*\s]*', '', lines[i + 1]).strip()
                m = re.match(r'(.+?)(?:\s*\((.+?)\))?$', next_line)
                if m:
                    name = m.group(1).strip()
                    status = m.group(2).strip() if m.group(2) else None
                    i += 1 

        elif re.match(r'^[##/*\s]*Credits', line, re.IGNORECASE):
            if i + 1 < len(lines):
                next_line = re.sub(r'^[##/*\s]*', '', lines[i + 1]).strip()
                author = next_line
                i += 1

        i += 1

    return {
        "name": name,
        "status": status,
        "author": author
    }

def should_ignore_file(path: Path):
    for d in IGNORE_DIRS:
        if d in path.parts:
            return True
    return False

def get_full_return_type(type_node, declarator_node, code_bytes):
    type_str = code_bytes[type_node.start_byte:type_node.end_byte].decode("utf-8").strip() if type_node else ""

    ptr_node = declarator_node
    while ptr_node and ptr_node.type == "pointer_declarator":
        type_str += " *"
        ptr_node = ptr_node.child_by_field_name("declarator")

    return type_str

def get_typedef_type(type_node, declarator_node, code_bytes):
    type_str = code_bytes[type_node.start_byte:type_node.end_byte].decode("utf-8").strip() if type_node else ""

    node = declarator_node
    while node:
        if node.type == "pointer_declarator":
            type_str += " *"
            node = node.child_by_field_name("declarator")
        elif node.type == "function_declarator":
            params_node = node.child_by_field_name("parameters")
            params = []
            if params_node:
                for p in params_node.children:
                    if p.type == "parameter_declaration":
                        p_type_node = p.child_by_field_name("type")
                        p_decl_node = p.child_by_field_name("declarator")
                        p_type = code_bytes[p_type_node.start_byte:p_type_node.end_byte].decode("utf-8").strip() if p_type_node else ""
                        p_name = code_bytes[p_decl_node.start_byte:p_decl_node.end_byte].decode("utf-8").strip() if p_decl_node else ""
                        params.append(f"{p_type} {p_name}".strip())
            type_str += f" ({', '.join(params)})"
            node = node.child_by_field_name("declarator")
        else:
            break

    return type_str


def extract_typedef_name(declarator_node, code_bytes):
    node = declarator_node
    while node:
        if node.type in ("pointer_declarator", "function_declarator"):
            node = node.child_by_field_name("declarator")
        else:
            break
    if node:
        return code_bytes[node.start_byte:node.end_byte].decode("utf-8").strip()
    return None


def extract_function_name_and_params(declarator_node, code_bytes):
    node = declarator_node
    params_node = None
    while True:
        if node.type == "pointer_declarator":
            node = node.child_by_field_name("declarator")
        elif node.type == "function_declarator":
            params_node = node.child_by_field_name("parameters")
            node = node.child_by_field_name("declarator")
        else:
            break

    func_name = code_bytes[node.start_byte:node.end_byte].decode("utf-8").strip() if node else None

    parameters = []
    if params_node:
        for p in params_node.children:
            if p.type == "parameter_declaration":
                p_type_node = p.child_by_field_name("type")
                p_decl_node = p.child_by_field_name("declarator")
                p_type = code_bytes[p_type_node.start_byte:p_type_node.end_byte].decode("utf-8").strip() if p_type_node else None
                p_name = code_bytes[p_decl_node.start_byte:p_decl_node.end_byte].decode("utf-8").strip() if p_decl_node else None
                parameters.append({"type": p_type, "name": p_name})

    return func_name, parameters

def extract_function_qualifiers(node, code_bytes):
    qualifiers = []
    for child in node.children:
        if child.type == "storage_class_specifier" or child.type == "type_qualifier":
            text = code_bytes[child.start_byte:child.end_byte].decode("utf-8").strip()
            if text:
                qualifiers.append(text)
        elif child.type == "function_specifier": 
            text = code_bytes[child.start_byte:child.end_byte].decode("utf-8").strip()
            if text:
                qualifiers.append(text)
    return qualifiers

def is_function_prototype(declarator):
    node = declarator
    while node:
        if node.type == "function_declarator":
            return True
        next_node = None
        for field in ("declarator", "inner", "child"):
            child = node.child_by_field_name(field)
            if child:
                next_node = child
                break
        if not next_node:
            return False
        node = next_node
    return False

def parse_c_types_and_functions(filename):
    functions = []
    globals_vars = []
    structs = []
    enums = []
    typedefs = []
    defines = []

    code_bytes = Path(filename).read_bytes()
    tree = parser.parse(code_bytes)
    root = tree.root_node

    def traverse(node):
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")
            type_node = node.child_by_field_name("type")
        
            if declarator:
                return_type = get_full_return_type(type_node, declarator, code_bytes)
                qualifiers = extract_function_qualifiers(node, code_bytes)
                func_name, parameters = extract_function_name_and_params(declarator, code_bytes)

                functions.append({
                    "name": func_name,
                    "return_type": return_type,
                    "parameters": parameters,
                    "qualifiers": qualifiers,
                    "line": node.start_point[0] + 1
                })

        elif node.type == "declaration":
            declarator = node.child_by_field_name("declarator")
            type_node = node.child_by_field_name("type")
        
            if declarator and is_function_prototype(declarator):
                return_type = get_full_return_type(type_node, declarator, code_bytes)
                qualifiers = extract_function_qualifiers(node, code_bytes)
                func_name, parameters = extract_function_name_and_params(declarator, code_bytes)
        
                functions.append({
                    "name": func_name,
                    "return_type": return_type,
                    "parameters": parameters,
                    "qualifiers": qualifiers,
                    "line": node.start_point[0] + 1,
                })
            else:
                var_name = extract_typedef_name(declarator, code_bytes) if declarator else None
                var_type = code_bytes[type_node.start_byte:type_node.end_byte].decode("utf-8").strip() if type_node else None
                qualifiers = extract_function_qualifiers(node, code_bytes) 
        
                value_node = node.child_by_field_name("value")
                lines = code_bytes.decode("utf-8").splitlines()
                value = code_bytes[value_node.start_byte:value_node.end_byte].decode("utf-8").strip() if value_node else None
                if var_name and not "#define" in (lines[node.start_point[0]]):
                    globals_vars.append({
                        "name": var_name,
                        "type": var_type,
                        "qualifiers": qualifiers,
                        "value": value,
                        "line": node.start_point[0] + 1
                    })
        
        elif node.type == "struct_specifier":
            name_node = node.child_by_field_name("name")
            name = code_bytes[name_node.start_byte:name_node.end_byte].decode("utf-8") if name_node else None

            members = []
            body_node = node.child_by_field_name("body")
            if body_node:
                for idx, field in enumerate(body_node.children):
                    if field.type == "field_declaration":
                        type_node = field.child_by_field_name("type")
                        name_node = field.child_by_field_name("declarator")
                        member_name = code_bytes[name_node.start_byte:name_node.end_byte].decode("utf-8") if name_node else None
                        member_type = code_bytes[type_node.start_byte:type_node.end_byte].decode("utf-8") if type_node else None
                        members.append({
                            "name": member_name,
                            "type": member_type,
                            "line": field.start_point[0] + 1,
                            "index": idx
                        })

            if len(members) > 0:
                structs.append({
                    "name": name,
                    "members": members,
                    "line": node.start_point[0] + 1,
                    "start_byte": node.start_byte,
                    "end_byte": node.end_byte
                })

        # Typedefs
        elif node.type == "type_definition":
            declarator_node = node.child_by_field_name("declarator")
            name = extract_typedef_name(declarator_node, code_bytes)
            typedefs.append({
                "name": name,
                "type": get_typedef_type(node.child_by_field_name("type"), node.child_by_field_name("declarator"), code_bytes),
                "line": node.start_point[0] + 1,
                "start_byte": node.start_byte,
                "end_byte": node.end_byte
            })
            

        # Enums
        elif node.type == "enum_specifier":
            body_node = node.child_by_field_name("body")
            if body_node:
                name_node = node.child_by_field_name("name")
                name = code_bytes[name_node.start_byte:name_node.end_byte].decode("utf-8") if name_node else None

                members = []
                for idx, enumerator in enumerate(body_node.children):
                    if enumerator.type == "enumerator":
                        enum_name_node = enumerator.child_by_field_name("name")
                        enum_value_node = enumerator.child_by_field_name("value")
                        enum_name = code_bytes[enum_name_node.start_byte:enum_name_node.end_byte].decode("utf-8") if enum_name_node else None
                        enum_value = code_bytes[enum_value_node.start_byte:enum_value_node.end_byte].decode("utf-8") if enum_value_node else None
                        members.append({
                            "name": enum_name,
                            "value": enum_value,
                            "line": enumerator.start_point[0] + 1,
                            "index": idx
                        })

                enums.append({
                    "name": name,
                    "members": members,
                    "line": node.start_point[0] + 1,
                    "start_byte": node.start_byte,
                    "end_byte": node.end_byte
                        })
        if node.type in ("preproc_def", "preproc_directive"):
            # Only handle #define
            lines = code_bytes.decode("utf-8").splitlines()
            start_line = node.start_point[0]
            end_line = node.end_point[0]
        
            # Gather the full multi-line macro
            full_text = lines[start_line]
        
            current_line = start_line
            while full_text.rstrip().endswith("\\") and current_line + 1 < len(lines):
                current_line += 1
                full_text = full_text.rstrip("\\") + "\n" + lines[current_line]
        
            text = full_text.strip()
            if text.startswith("#define"):
                parts = text[len("#define"):].strip().split(None, 1)
                name_and_params = parts[0]
                raw_text = parts[1] if len(parts) > 1 else ""
        
                # Handle function-like macros
                if "(" in name_and_params and name_and_params.endswith(")"):
                    idx = name_and_params.index("(")
                    name = name_and_params[:idx]
                    params_str = name_and_params[idx + 1:-1]
                    params = [p.strip() for p in params_str.split(",")] if params_str else []
                else:
                    name = name_and_params
                    params = None
        
                # Escape backslashes for JSON
                raw_text_escaped = raw_text.replace("\\", "\\\\")
        
        
                defines.append({
                    "name": name,
                    "params": params,
                    "raw_text": raw_text_escaped,
                    "line": start_line + 1
                })
        
        # Recurse
        for child in node.children:
            traverse(child)

    traverse(root)

    return {
        "functions": functions,
        "types": {
            "structs": structs,
            "enums": enums,
            "typedefs": typedefs,
            "globals": globals_vars,
        },
       "defines": defines
    }


def extract_commits(md_text: str):
    commits = []
    for match in COMMIT_RE.finditer(md_text):
        commits.append({
            "hash": match.group(1),
            "start_idx": match.start(),
            "end_idx": match.end()
        })
    return commits


def extract_idea_refs(text: str):
    refs = []
    for m in IDEA_REF_RE.finditer(text):
        refs.append({
            "string": m.group(1),
            "start_idx": m.start(),
            "end_idx": m.end()
        })
    return refs

def extract_audience(md_text: str):
    lines = md_text.splitlines()
    cleaned_lines = []
    audience = None
    skip_next = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        stripped = re.sub(r'^\s*(/\*+|\*+|//+)?\s*', '', line)

        m = re.match(r'^(#{1,6})\s*Audience:?\s*(.*)$', stripped, re.IGNORECASE)
        if m:
            inline_value = m.group(2).strip()
            if inline_value:
                audience = inline_value
            elif i + 1 < len(lines):
                next_line = re.sub(r'^\s*(/\*+|\*+|//+)?\s*', '', lines[i + 1]).strip()
                audience = next_line
                skip_next = True
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines), audience

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

            md_text, audience = extract_audience(md_text)
            metadata = extract_metadata(md_text)
            if audience:
                metadata["audience"] = audience

            refs["bugs"] = extract_bugs(md_text)
            refs["commits"] = extract_commits(md_text)
            refs["idea_refs"] = extract_idea_refs(md_text)

            ideas.append({
                "path": str(path),
                "name": name.strip(),
                "size": size,
                "start_line": idx + 1,
                "end_line": start_idx,
                "raw_text": raw_text,
                "content_md": md_text,
                "metadata": metadata,
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

        if re.match(r'^\s*\*/\s*$', line):
            continue

        line = re.sub(r'^\s*/\s*$', '', line)
        if not line.strip():
            continue

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

        if re.match(r'^##{1,6}\s*Bugs', stripped):
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

    if should_ignore_file(input_file):
        sys.exit(0)

    if not input_file.is_file():
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit(1)

    full_text = Path(input_file).read_text(encoding="utf-8")

    title = extract_file_title(full_text)
    ideas = extract_ideas_from_file(input_file)
    type_info = parse_c_types_and_functions(str(input_file))

    output = {
        "file": str(input_file),
        "title": title,
        "c_parse": type_info,
        "ideas": ideas
    }

    write_ideas_to_json(output, output_json)

if __name__ == "__main__":
    main()

