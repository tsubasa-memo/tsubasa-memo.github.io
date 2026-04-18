#!/usr/bin/env python3
"""ツバサのメモ帳 検索インデックス生成スクリプト

除外条件:
- 明示的exclude（404ページ、AdSense申請用ページ）
- <header>タグを持たないファイル（GSC認証、preview、サムネ比較等の内部ユーティリティ）
"""
import os, re, json, glob

def extract_record(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    t = re.search(r'<title>([^<]+)</title>', html)
    d = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    k = re.search(r'<meta\s+name="keywords"\s+content="([^"]+)"', html)
    body = html
    body = re.sub(r'<head\b[^>]*>.*?</head>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<noscript[^>]*>.*?</noscript>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = re.sub(r'&nbsp;', ' ', body)
    body = re.sub(r'&amp;', '&', body)
    body = re.sub(r'&lt;', '<', body)
    body = re.sub(r'&gt;', '>', body)
    body = re.sub(r'&quot;', '"', body)
    body = re.sub(r'&#\d+;|&\w+;', ' ', body)
    body = re.sub(r'\s+', ' ', body).strip()
    return {
        'u': path.replace('\\', '/'),
        't': t.group(1).strip() if t else '',
        'd': d.group(1).strip() if d else '',
        'k': k.group(1).strip() if k else '',
        'b': body,
    }

def should_include(path):
    """記事として検索対象にすべきか判定"""
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if not re.search(r'<header[\s>]', html, re.IGNORECASE):
        return False
    return True

def main():
    explicit_exclude = {'404.html', 'adsense-application.html'}

    paths = [p for p in sorted(glob.glob('*.html')) if p not in explicit_exclude]
    paths += sorted(glob.glob('glossary/*.html'))

    included, excluded = [], []
    for p in paths:
        if should_include(p):
            included.append(p)
        else:
            excluded.append(p)

    records = [extract_record(p) for p in included]
    with open('search-index.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, separators=(',', ':'))

    size = os.path.getsize('search-index.json')
    print(f'スキャン対象: {len(paths)}ファイル')
    print(f'インデックス登録: {len(included)}ファイル')
    print(f'除外: 明示{len(explicit_exclude & set(paths))}件 + <header>なし{len(excluded)}件')
    if excluded:
        print(f'  <header>なしで除外されたファイル:')
        for p in excluded:
            print(f'    - {p}')
    print(f'サイズ: {size:,} bytes ({size/1024:.1f} KB)')

if __name__ == '__main__':
    main()
