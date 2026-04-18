#!/usr/bin/env python3
"""
glossary-linker.py
==================
用語集（/glossary/*.html）へのインラインリンクを、指定した記事に対して
初出1回だけリンク化するツール。既存のリンクは保護される。

使い方:
    python3 scripts/glossary-linker.py          # dry-run（差分プレビューのみ）
    python3 scripts/glossary-linker.py --apply  # 実際にファイル書き換え

設計:
- 対象記事は WHITELIST で管理（レタッチ・ささげ系17記事）
- スラッグ→表示語の対応表は /glossary/index.html から自動抽出
- 除外ゾーン（head/script/style/見出し/既存<a>/blockquote/画像等）は
  プレースホルダー退避で保護
- 除外用語（EXCLUDED_SLUGS）は一律スキップ

新しい記事を対象に追加したいとき:
    WHITELIST リストに記事ファイル名を追記

用語集に新語を追加したとき:
    /glossary/index.html に .term-card を追加するだけで自動反映される
    （このスクリプト側の変更は不要）
"""

import re
import sys
from pathlib import Path
from html.parser import HTMLParser

# ============================================
# 設定セクション
# ============================================

# 対象記事（ホワイトリスト）
# 新記事を対象に追加する場合はここに追記
WHITELIST = [
    "retouch-cost-guide.html",
    "retouch-services.html",
    "retouch-apps.html",
    "retouch-outsource-tips.html",
    "retouch-pricing-database.html",
    "what-is-retouch.html",
    "ai-retouch-limits.html",
    "personal-retouch-order.html",
    "background-cutout-outsource.html",
    "background-white.html",
    "image-editing-outsource.html",
    "sasage-outsource.html",
    "sasage-outsource-cost.html",
    "ec-product-photo-service.html",
    "product-photo-diy-vs-outsource.html",
    "product-photo-retouch.html",
    "id-photo.html",
]

# 除外用語（リンク化しない）
# 文脈依存でリンクが不自然になる語をここで一律除外
EXCLUDED_SLUGS = {
    "banner",           # 「バナー」= 広告バナー/Photoshopバナー/単なる装飾画像、文脈により意味が散る
    "layer",            # 「レイヤー」= Photoshopユーザーには既知、リンク不要
    "rgb-cmyk",         # 「RGB」= ピクセル値指定等、色モード以外の文脈でも出現
    "session-pv-uu",    # 「セッション」= PCセッション等、統計指標以外でも使われる
    "ui-ux",            # 「UI」= 一般語と混同
}

# 対象外とする短すぎる語（ただし現状の用語集には該当なし。予防的設定）
MIN_TERM_LENGTH = 2

# 除外ゾーンの正規表現
EXCLUSION_PATTERNS = [
    (r'<head\b[^>]*>.*?</head>', re.DOTALL | re.IGNORECASE),
    (r'<script\b[^>]*>.*?</script>', re.DOTALL | re.IGNORECASE),
    (r'<style\b[^>]*>.*?</style>', re.DOTALL | re.IGNORECASE),
    (r'<h[1-6]\b[^>]*>.*?</h[1-6]>', re.DOTALL | re.IGNORECASE),
    (r'<a\b[^>]*>.*?</a>', re.DOTALL | re.IGNORECASE),
    (r'<blockquote\b[^>]*>.*?</blockquote>', re.DOTALL | re.IGNORECASE),
    (r'<(img|meta|link|input|source|track|area|br|hr|wbr)\b[^>]*/?>', re.IGNORECASE),
]

# CSSが追加されたか判定するマーカー
CSS_MARKER = "a.glossary-inline{"
CSS_BLOCK = (
    "\n/* ── Glossary inline link ── */\n"
    "a.glossary-inline{color:var(--accent);text-decoration:none;"
    "border-bottom:1px dotted var(--accent);padding-bottom:1px}\n"
    "a.glossary-inline:hover{border-bottom:1px solid var(--accent);"
    "text-decoration:none}\n"
)

# リポジトリルート
REPO_ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_INDEX = REPO_ROOT / "glossary" / "index.html"


# ============================================
# 用語集トップからスラッグ↔表示語の対応表を抽出
# ============================================

class TermCardParser(HTMLParser):
    """
    /glossary/index.html から以下の構造を抽出:
      <div class="term-card">
        <div class="term-name">PNG</div>
        ...
        <a href="/glossary/png.html" class="term-more">...</a>
      </div>
    """
    def __init__(self):
        super().__init__()
        self.in_card = False
        self.in_term_name = False
        self.current_name = []
        self.current_href = None
        self.results = {}  # {slug: display_term}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get("class", "").split()
        if tag == "div" and "term-card" in classes:
            self.in_card = True
            self.current_name = []
            self.current_href = None
        elif self.in_card and tag == "div" and "term-name" in classes:
            self.in_term_name = True
        elif self.in_card and tag == "a":
            href = attrs_dict.get("href", "")
            m = re.match(r'/glossary/([a-z0-9-]+)\.html', href)
            if m:
                self.current_href = m.group(1)

    def handle_endtag(self, tag):
        if tag == "div" and self.in_term_name:
            self.in_term_name = False
        elif tag == "div" and self.in_card and self.current_href and self.current_name:
            name = "".join(self.current_name).strip()
            if name and self.current_href not in self.results:
                self.results[self.current_href] = name
            self.in_card = False
            self.current_name = []
            self.current_href = None

    def handle_data(self, data):
        if self.in_term_name:
            self.current_name.append(data)


def load_term_map():
    """用語集トップから {slug: 表示語} を返す"""
    if not GLOSSARY_INDEX.exists():
        print(f"ERROR: {GLOSSARY_INDEX} が見つかりません")
        sys.exit(1)

    parser = TermCardParser()
    parser.feed(GLOSSARY_INDEX.read_text(encoding="utf-8"))

    if not parser.results:
        print("ERROR: /glossary/index.html から term-card を検出できませんでした")
        print("  HTMLの構造が変わった可能性があります。スクリプトのパーサーを確認してください。")
        sys.exit(1)

    return parser.results


# ============================================
# 記事単位の処理
# ============================================

def stash_exclusions(html):
    """除外ゾーンをプレースホルダーに退避"""
    placeholders = {}
    counter = [0]

    def replacer(m):
        counter[0] += 1
        key = f"\x00PLACEHOLDER_{counter[0]}\x00"
        placeholders[key] = m.group(0)
        return key

    for pattern, flags in EXCLUSION_PATTERNS:
        html = re.sub(pattern, replacer, html, flags=flags)

    return html, placeholders


def unstash_exclusions(html, placeholders):
    """プレースホルダーを元に戻す"""
    for key, original in placeholders.items():
        html = html.replace(key, original)
    return html


def add_css_if_missing(html):
    """既存CSSに glossary-inline 定義がなければ追加"""
    if CSS_MARKER in html:
        return html, False
    idx = html.find("</style>")
    if idx == -1:
        return html, False
    return html[:idx] + CSS_BLOCK + html[idx:], True


def placeholders_content(placeholders):
    """プレースホルダーに退避された内容の全結合"""
    return "".join(placeholders.values())


def process_article(filepath, term_map):
    """
    1記事を処理。
    """
    path = Path(filepath)
    if not path.exists():
        return None

    html_before = path.read_text(encoding="utf-8")
    html = html_before

    # CSS追加
    html, css_added = add_css_if_missing(html)

    # 除外ゾーン退避
    html, placeholders = stash_exclusions(html)

    # 用語を長い順にソート（部分マッチ防止）
    sorted_terms = sorted(term_map.items(), key=lambda x: -len(x[1]))

    new_links = []
    existing_links = []
    no_match = []
    skipped_excluded = []

    stashed_text = placeholders_content(placeholders)

    for slug, term in sorted_terms:
        if slug in EXCLUDED_SLUGS:
            if f'/glossary/{slug}.html' in html_before:
                skipped_excluded.append((term, slug))
            continue

        if len(term) < MIN_TERM_LENGTH:
            continue

        # 既にこのスラッグへのリンクが退避ゾーンに存在するか
        already_linked = f'/glossary/{slug}.html' in stashed_text

        pattern = re.escape(term)
        replacement = f'<a href="/glossary/{slug}.html" class="glossary-inline">{term}</a>'
        html_new, n = re.subn(pattern, replacement, html, count=1)

        if n > 0:
            new_links.append((term, slug))
            html = html_new
        elif already_linked:
            existing_links.append((term, slug))
        else:
            no_match.append((term, slug))

    html = unstash_exclusions(html, placeholders)

    if "PLACEHOLDER_" in html:
        print(f"  ✗ {filepath}: プレースホルダー残存。処理を中止します")
        sys.exit(1)

    return {
        'file': filepath,
        'css_added': css_added,
        'new_links': new_links,
        'existing_links': existing_links,
        'no_match': no_match,
        'skipped_excluded': skipped_excluded,
        'html_before': html_before,
        'html_after': html,
    }


def count_diff_lines(before, after):
    """変更前後の差分行数を雑に見積もる"""
    if before == after:
        return 0
    before_lines = before.splitlines()
    after_lines = after.splitlines()
    return abs(len(after_lines) - len(before_lines)) + \
           sum(1 for a, b in zip(before_lines, after_lines) if a != b)


# ============================================
# メイン処理
# ============================================

def main():
    apply_mode = "--apply" in sys.argv

    print("=" * 70)
    if apply_mode:
        print("■ glossary-linker.py  [APPLY モード：実際に書き換えます]")
    else:
        print("■ glossary-linker.py  [DRY-RUN モード：差分プレビューのみ]")
        print("   実際に書き換えるには --apply を付けて再実行してください")
    print("=" * 70)

    term_map = load_term_map()
    print(f"\n用語集から読み込んだ用語数: {len(term_map)}")
    print(f"除外指定の用語: {len(EXCLUDED_SLUGS)}（{', '.join(sorted(EXCLUDED_SLUGS))}）")
    print(f"対象記事数: {len(WHITELIST)}")

    print("\n" + "=" * 70)
    print("■ 記事別の処理結果")
    print("=" * 70)

    total_new = 0
    total_existing = 0
    applied_files = []
    warnings = []

    for filename in WHITELIST:
        filepath = REPO_ROOT / filename
        if not filepath.exists():
            print(f"\n[{filename}] ✗ ファイルなし")
            warnings.append(f"ファイルなし: {filename}")
            continue

        result = process_article(str(filepath), term_map)
        if not result:
            continue

        new_count = len(result['new_links'])
        existing_count = len(result['existing_links'])
        total_new += new_count
        total_existing += existing_count

        if new_count > 0 or result['css_added']:
            print(f"\n[{filename}]  +{new_count}新規 / {existing_count}既存")
            if result['css_added']:
                print(f"  + CSS: glossary-inline を追加")
            for term, slug in result['new_links']:
                print(f"  + 新規リンク: {term}  → /glossary/{slug}.html")
            diff_lines = count_diff_lines(result['html_before'], result['html_after'])
            if diff_lines > 40:
                warn = f"{filename}: 差分{diff_lines}行（40超過）"
                warnings.append(warn)
                print(f"  ⚠ 差分{diff_lines}行（上限目安40を超過）")

            if apply_mode and result['html_before'] != result['html_after']:
                Path(filepath).write_text(result['html_after'], encoding="utf-8")
                applied_files.append(filename)

    print("\n" + "=" * 70)
    print("■ サマリ")
    print("=" * 70)
    print(f"新規リンク化: {total_new}本")
    print(f"既存リンク（保護済み）: {total_existing}本")

    if warnings:
        print(f"\n⚠ 警告 ({len(warnings)}件):")
        for w in warnings:
            print(f"  - {w}")

    if apply_mode:
        print(f"\n✓ 書き換え実施: {len(applied_files)}ファイル")
        if applied_files:
            print("   以下を手動で確認・コミットしてください:")
            print("     git diff")
            print("     git add " + " ".join(applied_files))
            print("     git commit -m 'glossary-linker: 用語集リンクを更新'")
    else:
        if total_new > 0:
            print(f"\n→ 実際に書き換えるには: python3 scripts/glossary-linker.py --apply")
        else:
            print("\n→ 変更なし。現状のまま。")


if __name__ == "__main__":
    main()
