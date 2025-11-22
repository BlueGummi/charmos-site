#!/usr/bin/env python3
import os, sys, shutil
from pathlib import Path

DOCS_ROOT = Path("./docs")
MAX_LINES = 300

def print_single_line(*args, **kwargs):
    text = " ".join(str(arg) for arg in args)
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    spaces_to_clear = max(terminal_width - len(text), 0)
    output = "\r" + text + " " * spaces_to_clear

    flush = kwargs.get("flush", True)

    sys.stdout.write(output)
    if flush:
        sys.stdout.flush()

def merge_small_dirs(root: Path):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        dir_path = Path(dirpath)

        if dirnames:
            continue

        md_files = [f for f in dir_path.glob("*.md") if f.is_file()]
        if not md_files:
            continue

        total_lines = 0
        file_contents = []
        for f in md_files:
            content = f.read_text(encoding="utf-8")
            total_lines += len(content.splitlines())
            file_contents.append((f, content))

        if total_lines <= MAX_LINES:
            parent_dir = dir_path.parent
            merged_file_path = parent_dir / f"{dir_path.name}.md"

            with merged_file_path.open("w", encoding="utf-8") as out:
                for f, content in file_contents:
                    out.write(content)
                    out.write("\n\n") 

            for f, _ in file_contents:
                f.unlink()
            dir_path.rmdir()

            print_single_line(f"merged {len(file_contents)} files → {merged_file_path}")

if __name__ == "__main__":
    merge_small_dirs(DOCS_ROOT)

