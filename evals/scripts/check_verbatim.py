#!/usr/bin/env python3
"""Check that every quoted line (`> ...`) under skills/tidy-first/references/
exists verbatim in the book chapters at a base git ref (default: main).

Usage: check_verbatim.py [--base REF] [--refs DIR]
Exit 1 if any quoted line is new or altered, or if a tidying file lost its
`*Tidy First?*, ch. N, pp. A–B.` citation line.
"""
import argparse, pathlib, re, subprocess, sys

def quoted_lines(text):
    return [l.rstrip() for l in text.splitlines() if l.startswith(">")]

def base_quotes(base):
    files = subprocess.run(["git", "ls-tree", "-r", "--name-only", base],
                           capture_output=True, text=True, check=True).stdout.split()
    quotes = set()
    for f in files:
        if not f.endswith(".md"):
            continue
        if not re.match(r"^(examples|managing|theory|skills/tidy-first/references)/", f):
            continue
        blob = subprocess.run(["git", "show", f"{base}:{f}"], capture_output=True, text=True, check=True).stdout
        quotes.update(quoted_lines(blob))
    return quotes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="main")
    ap.add_argument("--refs", default="skills/tidy-first/references")
    a = ap.parse_args()
    known = base_quotes(a.base)
    bad = 0
    for path in sorted(pathlib.Path(a.refs).rglob("*.md")):
        text = path.read_text()
        for n, line in enumerate(text.splitlines(), 1):
            if line.startswith(">") and line.rstrip() not in known:
                print(f"{path}:{n}: quoted line not in {a.base}: {line[:90]}")
                bad += 1
        if "/tidyings/" in str(path) and not re.search(r"^\*Tidy First\?\*, ch\. \d+, pp?\. ", text, re.M):
            print(f"{path}: missing citation line")
            bad += 1
    print(f"{'FAIL' if bad else 'OK'}: {bad} problems; {len(known)} known quoted lines in {a.base}")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
