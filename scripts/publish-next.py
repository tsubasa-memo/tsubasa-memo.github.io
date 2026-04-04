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
    pub_date = entry["publish_utc"][:10].replace("-", ".")
    date_html = f'<div class="card-dates"><span class="card-date-pub">公開 {pub_date}</span></div>'
    return (
        f'<div class="article-card" data-cat="{entry["cat"]}">\n'
        f'<a href="{entry["slug"]}.html">\n'
        f'<div class="card-thumb"><img src="thumbs/{entry["slug"]}.svg" alt="" width="320" height="180"></div>\n'
        f'<div class="card-body">\n'
        f'{date_html}\n'
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
    1. AI タブがなければ追加
    2. 記事カードを article-list 先頭に挿入
    3. count を更新
    """
    html = archive_html

    # 1. filter-tab に data-cat="ai" がなければ career の前に追加
    if 'data-cat="ai"' not in html:
        html = html.replace(
            '<span class="filter-tab" data-cat="career">',
            '<span class="filter-tab" data-cat="ai">AI</span>\n<span class="filter-tab" data-cat="career">'
        )

    # 2. 記事カードを挿入（最新=一番上）
    # articles は order 昇順なので、最後の要素が最新
    cards_html = []
    for article in articles:
        cards_html.append(build_card_html(article))

    # 最新が一番上になるよう逆順で結合
    cards_block = "\n".join(reversed(cards_html))

    # article-list の直後に挿入
    html = html.replace(
        '<div class="article-list">\n',
        '<div class="article-list">\n' + cards_block + "\n"
    )

    # 3. count を更新
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

    # article-dates.json に公開日を追記
    dates_path = REPO_ROOT / "article-dates.json"
    with open(dates_path, encoding="utf-8") as f:
        article_dates = json.load(f)
    for article in articles:
        slug = article["slug"]
        if slug not in article_dates:
            article_dates[slug] = {"pub_date": article["publish_utc"][:10]}
    with open(dates_path, "w", encoding="utf-8") as f:
        json.dump(article_dates, f, indent=2, ensure_ascii=False)
    print("Updated article-dates.json")

    print("Done.")


if __name__ == "__main__":
    main()
