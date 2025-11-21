#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path
import os

REPO_URL = "https://github.com/bluegummi/charmos.git"
CLONE_DIR = Path("./charmos")
JSON_OUT = Path("./json_output")
MD_OUT = Path("./docs")
LIMINE_URL = "https://github.com/limine-bootloader/limine"
LIMINE_DIR = Path("./limine")

SOURCE_DIRS = [
    "kernel",   
    "include", 
]

def clone_repo():
    if CLONE_DIR.exists():
        return;

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

    for f in files:
        json_out_path = json_filename_for_source(f)
        print(f"  → {f.relative_to(CLONE_DIR)} → {json_out_path.name}")

        subprocess.check_call([
            "python3", "make_json.py",
            str(f),
            str(json_out_path)
        ])

def run_make_md():
    subprocess.check_call([
        "python3", "make_md.py",
        str(JSON_OUT)
    ])

def delete_empty_markdown():
    for path in MD_OUT.glob("**/*.md"):
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            print(f"  → Removing empty: {path}")
            path.unlink()

def main():
    subprocess.check_call([
        "rm", "-rf", "json_output",
    ])
    
    subprocess.check_call([
        "rm", "-rf", "docs",
    ])

    clone_repo()
    prepare_output_dirs()
    run_make_json()
    run_make_md()
    delete_empty_markdown()
    subprocess.check_call([
        "python3", "cleanup.py",
    ])


    print("SUCCESS")

if __name__ == "__main__":
    main()

