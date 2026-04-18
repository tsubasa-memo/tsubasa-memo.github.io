#!/usr/bin/env python3
"""ツバサのメモ帳 検索インデックス生成スクリプト"""
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

def main():
    exclude = {'404.html', 'adsense-application.html'}
    paths = [p for p in sorted(glob.glob('*.html')) if p not in exclude]
    paths += sorted(glob.glob('glossary/*.html'))
    records = [extract_record(p) for p in paths]
    with open('search-index.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, separators=(',', ':'))
    size = os.path.getsize('search-index.json')
    print(f'対象: {len(paths)}ファイル  サイズ: {size/1024:.1f} KB  レコード: {len(records)}')

if __name__ == '__main__':
    main()
