#!/usr/bin/env python3
"""
publish-next.py
drafts/ の未公開記事を1本 draft ブランチに公開する。
launchd から 30780秒（8h33m）間隔で呼び出されることを想定。
"""

import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

REPO = Path.home() / "Desktop" / "tsubasa-memo.github.io"
LOG = REPO / "publish.log"


def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(cmd: list, **kwargs):
    result = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kwargs)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()


def ensure_draft_branch():
    current = run(["git", "branch", "--show-current"])
    if current != "draft":
        log(f"現在のブランチ: {current} → draft に切り替えます")
        # 未コミット変更があればスタッシュ
        status = run(["git", "status", "--porcelain"])
        stashed = False
        if status:
            run(["git", "stash", "--include-untracked"])
            stashed = True
        run(["git", "checkout", "draft"])
        if stashed:
            run(["git", "stash", "pop"])


def find_next_draft() -> Optional[Path]:
    drafts_dir = REPO / "drafts"
    for draft in sorted(drafts_dir.iterdir()):
        if not draft.is_dir() or draft.name == "index.html":
            continue
        # フォルダ名: 2026-04-01_ec-product-description
        parts = draft.name.split("_", 1)
        if len(parts) < 2:
            continue
        slug = parts[1]
        if not (REPO / f"{slug}.html").exists():
            return draft
    return None


def build_index_card(slug: str, title: str, desc: str, cat_label: str) -> str:
    return (
        f'<div class="article-card">\n'
        f'<a href="{slug}.html">\n'
        f'<div class="card-thumb"><img src="thumbs/{slug}.svg" alt="{title}" width="320" height="180"></div>\n'
        f'<div class="card-body">\n'
        f'<span class="card-num new">NEW</span>\n'
        f'<h2>{title}</h2>\n'
        f'<p class="card-desc">{desc}</p>\n'
        f'<span class="card-tag">{cat_label}</span>\n'
        f'</div>\n'
        f'</a>\n'
        f'</div>\n'
    )


def build_archive_card(slug: str, title: str, desc: str, cat: str, cat_label: str) -> str:
    return (
        f'<div class="article-card" data-cat="{cat}">\n'
        f'<a href="{slug}.html">\n'
        f'<div class="card-thumb"><img src="thumbs/{slug}.svg" alt="{title}" width="320" height="180"></div>\n'
        f'<div class="card-body">\n'
        f'<span class="card-num new">NEW</span>\n'
        f'<h2>{title}</h2>\n'
        f'<p class="card-desc">{desc}</p>\n'
        f'<span class="card-tag">{cat_label}</span>\n'
        f'</div>\n'
        f'</a>\n'
        f'</div>\n'
    )


def update_index(slug: str, title: str, desc: str, cat_label: str, current_ym: str):
    path = REPO / "index.html"
    content = path.read_text(encoding="utf-8")

    # 前回の NEW → 日付に
    content = content.replace(
        '<span class="card-num new">NEW</span>',
        f'<span class="card-num">{current_ym}</span>'
    )

    # 新カードを article-list の直後に挿入
    new_card = build_index_card(slug, title, desc, cat_label)
    content = content.replace(
        '<div class="article-list">\n',
        f'<div class="article-list">\n{new_card}',
        1
    )

    # 全XX件 カウント更新
    m = re.search(r'全(\d+)件', content)
    if m:
        new_count = int(m.group(1)) + 1
        content = re.sub(r'全\d+件', f'全{new_count}件', content)

    path.write_text(content, encoding="utf-8")
    log("index.html 更新完了")


def update_archive(slug: str, title: str, desc: str, cat: str, cat_label: str, current_ym: str):
    path = REPO / "archive.html"
    content = path.read_text(encoding="utf-8")

    # 前回の NEW → 日付に
    content = content.replace(
        '<span class="card-num new">NEW</span>',
        f'<span class="card-num">{current_ym}</span>'
    )

    # 新カードを article-list の直後に挿入
    new_card = build_archive_card(slug, title, desc, cat, cat_label)
    content = content.replace(
        '<div class="article-list">\n',
        f'<div class="article-list">\n{new_card}',
        1
    )

    # <span id="count">XX</span> 更新
    m = re.search(r'<span id="count">(\d+)</span>', content)
    if m:
        new_count = int(m.group(1)) + 1
        content = re.sub(r'<span id="count">\d+</span>', f'<span id="count">{new_count}</span>', content)

    path.write_text(content, encoding="utf-8")
    log("archive.html 更新完了")


def main():
    log("=== publish-next.py 開始 ===")

    os.chdir(REPO)

    try:
        ensure_draft_branch()
    except Exception as e:
        log(f"ブランチ切り替え失敗: {e}")
        sys.exit(1)

    draft = find_next_draft()
    if draft is None:
        log("公開待ちドラフトなし。全記事公開済みです。")
        sys.exit(0)

    folder = draft.name
    slug = folder.split("_", 1)[1]
    date_prefix = folder.split("_")[0]  # 2026-04-01
    current_ym = f"{date_prefix[:4]}.{date_prefix[5:7]}"  # 2026.04

    log(f"対象: {slug}（予定日: {date_prefix}）")

    # meta.json 読み込み
    with open(draft / "meta.json", encoding="utf-8") as f:
        meta = json.load(f)

    title = meta["title"]
    desc = meta["description"]
    cat = meta["category"]
    cat_label = meta["category_label"]

    # ファイルコピー
    shutil.copy(draft / f"{slug}.html", REPO / f"{slug}.html")
    log(f"{slug}.html → ルートにコピー")

    shutil.copy(draft / "og.png", REPO / "og" / f"{slug}.png")
    log(f"og/{slug}.png コピー")

    shutil.copy(draft / "thumb.svg", REPO / "thumbs" / f"{slug}.svg")
    log(f"thumbs/{slug}.svg コピー")

    # HTML 更新
    update_index(slug, title, desc, cat_label, current_ym)
    update_archive(slug, title, desc, cat, cat_label, current_ym)

    # git add / commit / push
    files = [
        f"{slug}.html",
        f"og/{slug}.png",
        f"thumbs/{slug}.svg",
        "index.html",
        "archive.html",
    ]
    run(["git", "add"] + files)
    run(["git", "commit", "-m", f"publish: {slug}（{date_prefix}）"])
    run(["git", "push", "origin", "HEAD:main"])

    log(f"=== 公開完了: {slug} ===\n")


if __name__ == "__main__":
    main()
