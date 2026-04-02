#!/usr/bin/env python3
"""
publish-next.py
GitHub Actions から8時間ごとに実行される記事自動公開スクリプト。
publish-schedule.json を読み、現在UTCを過ぎたスケジュールのうち
archive.html に未掲載の記事を archive.html と sitemap.xml に追加する。
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEDULE_PATH = REPO_ROOT / "publish-schedule.json"
ARCHIVE_PATH = REPO_ROOT / "archive.html"
SITEMAP_PATH = REPO_ROOT / "sitemap.xml"


def load_schedule():
    with open(SCHEDULE_PATH, encoding="utf-8") as f:
        return json.load(f)


def read_text(path):
    return path.read_text(encoding="utf-8")


def write_text(path, content):
    path.write_text(content, encoding="utf-8")


def find_pending_articles(schedule, archive_html):
    """publish_utc が過ぎていて archive.html に未掲載の記事を返す（order順）。"""
    now = datetime.now(timezone.utc)
    pending = []
    for entry in schedule:
        pub_time = datetime.fromisoformat(entry["publish_utc"].replace("Z", "+00:00"))
        if pub_time <= now:
            # href に slug が含まれていなければ未掲載
            if f'href="{entry["slug"]}.html"' not in archive_html:
                pending.append(entry)
    # order 順にソート
    pending.sort(key=lambda e: e["order"])
    return pending


def build_card_html(entry, is_newest=False):
    """記事カードHTMLを生成する。"""
    num_class = 'card-num new' if is_newest else 'card-num'
    num_text = 'NEW' if is_newest else entry["date_label"]
    return (
        f'<div class="article-card" data-cat="{entry["cat"]}">\n'
        f'<a href="{entry["slug"]}.html">\n'
        f'<div class="card-thumb"><img src="thumbs/{entry["slug"]}.svg" alt="" width="320" height="180"></div>\n'
        f'<div class="card-body">\n'
        f'<span class="{num_class}">{num_text}</span>\n'
        f'<h2>{entry["title"]}</h2>\n'
        f'<p class="card-desc">{entry["card_desc"]}</p>\n'
        f'<span class="card-tag">{entry["tag"]}</span>\n'
        f'</div>\n'
        f'</a>\n'
        f'</div>'
    )


def update_archive(archive_html, articles):
    """
    archive.html を更新して返す。
    1. 既存 NEW バッジを日付に置換
    2. AI タブがなければ追加
    3. 記事カードを article-list 先頭に挿入（最新のみ NEW）
    4. count を更新
    """
    html = archive_html

    # 1. 既存の NEW バッジを日付ラベルに変更
    html = html.replace(
        '<span class="card-num new">NEW</span>',
        '<span class="card-num">2026.04</span>'
    )

    # 2. filter-tab に data-cat="ai" がなければ career の前に追加
    if 'data-cat="ai"' not in html:
        html = html.replace(
            '<span class="filter-tab" data-cat="career">',
            '<span class="filter-tab" data-cat="ai">AI</span>\n<span class="filter-tab" data-cat="career">'
        )

    # 3. 記事カードを挿入（最新=一番上、最新のみ NEW バッジ）
    # articles は order 昇順なので、最後の要素が最新
    cards_html = []
    for i, article in enumerate(articles):
        is_newest = (i == len(articles) - 1)
        cards_html.append(build_card_html(article, is_newest=is_newest))

    # 最新が一番上になるよう逆順で結合
    cards_block = "\n".join(reversed(cards_html))

    # article-list の直後に挿入
    html = html.replace(
        '<div class="article-list">\n',
        '<div class="article-list">\n' + cards_block + "\n"
    )

    # 4. count を更新
    # 既存の記事数 + 追加記事数
    count_match = re.search(r'<span id="count">(\d+)</span>', html)
    if count_match:
        old_count = int(count_match.group(1))
        new_count = old_count + len(articles)
        html = html.replace(
            f'<span id="count">{old_count}</span>',
            f'<span id="count">{new_count}</span>'
        )

    return html


def update_sitemap(sitemap_xml, articles):
    """sitemap.xml に URL エントリを追加して返す。"""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entries = []
    for article in articles:
        entry = (
            f"  <url>\n"
            f"    <loc>https://tsubasa-memo.github.io/{article['slug']}.html</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"  </url>"
        )
        entries.append(entry)

    insert_block = "\n".join(entries)
    sitemap_xml = sitemap_xml.replace(
        "</urlset>",
        insert_block + "\n</urlset>"
    )
    return sitemap_xml


def main():
    schedule = load_schedule()
    archive_html = read_text(ARCHIVE_PATH)

    articles = find_pending_articles(schedule, archive_html)
    if not articles:
        print("No articles to publish.")
        return

    slugs = [a["slug"] for a in articles]
    print(f"Publishing {len(articles)} article(s): {', '.join(slugs)}")

    # archive.html 更新
    new_archive = update_archive(archive_html, articles)
    write_text(ARCHIVE_PATH, new_archive)
    print("Updated archive.html")

    # sitemap.xml 更新
    sitemap_xml = read_text(SITEMAP_PATH)
    new_sitemap = update_sitemap(sitemap_xml, articles)
    write_text(SITEMAP_PATH, new_sitemap)
    print("Updated sitemap.xml")

    print("Done.")


if __name__ == "__main__":
    main()
