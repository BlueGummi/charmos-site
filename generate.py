#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path
import os, sys

REPO_URL = "https://github.com/bluegummi/charmos.git"
CLONE_DIR = Path("./charmos")
JSON_OUT = Path("./json_output")
MD_OUT = Path("./docs")
LIMINE_URL = "https://github.com/limine-bootloader/limine"
LIMINE_DIR = Path("./limine")

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

SOURCE_DIRS = [
#    "kernel",   
    "include", 
]

def clone_repo():
    if CLONE_DIR.exists():
        return

    subprocess.check_call([
        "git", "clone", "--depth=1",
        REPO_URL,
        str(CLONE_DIR)
    ])

    subprocess.check_call(["git", "submodule", "init"], cwd=CLONE_DIR)
    subprocess.check_call(["git", "submodule", "update"], cwd=CLONE_DIR)

    tests_dir = CLONE_DIR / "kernel/uACPI/tests"
    if tests_dir.exists():
        shutil.rmtree(tests_dir)

    if not LIMINE_DIR.exists():
        subprocess.check_call([
            "git", "clone",
            "--branch=v9.x-binary",
            "--depth=1",
            LIMINE_URL,
            str(LIMINE_DIR)
        ])

def prepare_output_dirs():
    if JSON_OUT.exists():
        shutil.rmtree(JSON_OUT)
    JSON_OUT.mkdir(parents=True)

    MD_OUT.mkdir(parents=True, exist_ok=True)

def json_filename_for_source(file_path: Path) -> Path:
    parents = file_path.parts[-3:-1]
    name_bits = list(parents) + [file_path.stem]
    json_name = "_".join(name_bits) + ".json"
    return JSON_OUT / json_name

def run_make_json():
    files = []
    for dir_name in SOURCE_DIRS:
        dir_path = CLONE_DIR / dir_name
        if not dir_path.exists():
            continue
        files.extend(dir_path.rglob("*.c"))
        files.extend(dir_path.rglob("*.h"))

    files = [f for f in files if f.is_file()]

    if not files:
        return

    for i, f in enumerate(files, start=1):
        json_out_path = json_filename_for_source(f)
        progress = i / len(files)
        subprocess.check_call([
            "python3", "make_json.py",
            str(f),
            str(json_out_path)
        ])
        
        print_single_line(f"parsed source {f.relative_to(CLONE_DIR)} → {json_out_path.name}", progress=progress)

def run_make_md():
    subprocess.check_call([
        "python3", "make_md.py",
        str(JSON_OUT)
    ])

def delete_empty_markdown():
    for path in MD_OUT.glob("**/*.md"):
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            print_single_line(f" removing empty: {path}")
            path.unlink()

def copy_directory_indexes(src_root: Path, docs_root: Path):
    count = len(list(src_root.rglob("index.mdx")))
    for (i, index_file) in enumerate(src_root.rglob("index.mdx")):
        rel = index_file.relative_to(src_root)

        dest_path = docs_root / rel

        dest_path.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(index_file, dest_path)
        print_single_line(f"copied {index_file} → {dest_path}", progress = i / count)



def rename_directories_from_namefiles(root: Path):
    subdirs = [d for d in root.iterdir() if d.is_dir()]
    count = len(subdirs)

    for i, subdir in enumerate(subdirs):
        name_file = subdir / "dir_doc_name"

        if name_file.is_file():
            new_name = name_file.read_text(encoding="utf-8").strip()

            if new_name and new_name != subdir.name:
                new_path = subdir.parent / new_name

                if not new_path.exists():
                    print_single_line(
                        f"renaming {subdir} → {new_path}",
                        progress=i / max(count, 1)
                    )
                    subdir.rename(new_path)
                    subdir = new_path
                else:
                    print_single_line(
                        f"[SKIP exists] {subdir} → {new_path}",
                        progress=i / max(count, 1)
                    )

        rename_directories_from_namefiles(subdir)

def main():
    subprocess.check_call([
        "rm", "-rf", "json_output",
    ])
    
    subprocess.check_call([
        "rm", "-rf", "docs",
    ])

    clone_repo()
    print("initial repo clone and setup complete")
    rename_directories_from_namefiles(Path("charmos"))
    print("directory rename completed")
    prepare_output_dirs()
    print("output directory setup completed")
    run_make_json()
    print("JSON parsing completed")
    run_make_md()
    print("markdown generated")
    delete_empty_markdown()
    print("markdown cleaned")
    copy_directory_indexes(Path("charmos/include"), Path("docs"))
    print("directory indexes copied")

    print("complete.")


if __name__ == "__main__":
    main()

