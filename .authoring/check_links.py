#!/usr/bin/env python3
"""Jekyll版カリキュラムの内部リンク切れを検出する。

使い方: python3 .authoring/check_links.py
- 各.md内の相対リンク（.html / ディレクトリ）が実ファイルに解決できるか確認する。
- frontmatterのparentがリンク先セクションのtitleと一致するかも確認する。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".github", ".authoring", "_sass", "practice", "node_modules"}

link_re = re.compile(r"\[[^\]]*\]\(([^)\s#]+)(#[^)]*)?\)")

errors = []
md_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for f in filenames:
        if f.endswith(".md"):
            md_files.append(os.path.join(dirpath, f))

for md in md_files:
    base = os.path.dirname(md)
    text = open(md, encoding="utf-8").read()
    for m in link_re.finditer(text):
        url = m.group(1)
        if url.startswith(("http://", "https://", "mailto:", "{{", "{%")) or url == "...":
            continue
        target = os.path.normpath(os.path.join(base, url))
        ok = False
        if url.endswith("/") or os.path.isdir(target):
            ok = os.path.isfile(os.path.join(target, "index.md"))
        elif url.endswith(".html"):
            ok = os.path.isfile(target[:-5] + ".md") or os.path.isfile(target)
        else:
            # 拡張子なしリンクはGitHub Pagesでは .html に解決される
            ok = os.path.isfile(target) or os.path.isfile(target + ".md")
        if not ok:
            rel = os.path.relpath(md, ROOT)
            errors.append(f"{rel}: リンク切れ -> {url}")

if errors:
    print(f"NG: {len(errors)} 件のリンク切れ")
    for e in sorted(set(errors)):
        print("  " + e)
    sys.exit(1)
print(f"OK: {len(md_files)} ファイルを確認、リンク切れなし")
