#!/usr/bin/env python3
"""既存HTMLに検索UIを一括埋め込み（冪等）"""
import re, glob

SEARCH_HTML = '''<div class="site-search-wrap">
<div class="wrap">
<input type="search" id="site-search-input" placeholder="サービス名・キーワードで検索" autocomplete="off" aria-label="サイト内検索">
<div id="site-search-results" hidden></div>
</div>
</div>'''
MARKER = 'id="site-search-input"'

def process(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if MARKER in html:
        return 'skip'
    head_close = html.find('</head>')
    if head_close < 0: return 'err'
    html = html[:head_close] + '<link rel="stylesheet" href="/search.css">\n<script src="/search.js" defer></script>\n' + html[head_close:]
    header_close = html.find('</header>')
    if header_close < 0: return 'err'
    insert_at = header_close + len('</header>')
    html = html[:insert_at] + '\n' + SEARCH_HTML + html[insert_at:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    return 'updated'

def main():
    exclude = {'404.html'}
    paths = [p for p in sorted(glob.glob('*.html')) if p not in exclude]
    paths += sorted(glob.glob('glossary/*.html'))
    stats = {'updated': 0, 'skip': 0, 'err': 0}
    for p in paths:
        r = process(p)
        stats[r] = stats.get(r, 0) + 1
    print(f'対象: {len(paths)}  更新: {stats["updated"]}  既埋め込み: {stats["skip"]}  エラー: {stats["err"]}')

if __name__ == '__main__':
    main()
