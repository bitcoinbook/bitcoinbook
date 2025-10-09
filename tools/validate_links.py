#!/usr/bin/env python3
"""
Simple internal link validator for Mastering Bitcoin book files.
Scans all .adoc files and reports missing or broken local references.
"""

import os
import re

def find_broken_links(base_dir="."):
    adoc_files = [f for f in os.listdir(base_dir) if f.endswith(".adoc")]
    link_pattern = re.compile(r'<<([a-zA-Z0-9_\-]+)>>')
    missing = []

    for file in adoc_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        refs = link_pattern.findall(content)
        for ref in refs:
            if not any(ref in open(f2, encoding="utf-8").read() for f2 in adoc_files):
                missing.append((file, ref))
    return missing

if __name__ == "__main__":
    broken = find_broken_links()
    if not broken:
        print("✅ All internal links look valid.")
    else:
        print("⚠️  Broken links found:")
        for file, ref in broken:
            print(f" - {ref} in {file}")
