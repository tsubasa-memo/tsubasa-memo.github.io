#!/usr/bin/env python3
"""用語集20ページ一括生成スクリプト
Usage: python3 generate_glossary_20.py
Output: glossary/*.html (20ファイル)
"""

import json, os, re

TEMPLATE = r'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YYBFXHXMM6"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-YYBFXHXMM6');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6503265021738697" crossorigin="anonymous"></script>
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://tsubasa-memo.github.io/glossary/{slug}.html">
<meta property="og:site_name" content="ツバサのメモ帳">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://tsubasa-memo.github.io/glossary/{slug}.html">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
{jsonld}
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#f8f7f4;--text:#2d2d2d;--text-sub:#666;--accent:#2e6b8a;--accent-light:#e8f0f5;--border:#e0ddd8;--card:#fff;--link:#2e6b8a;--tag-bg:#f2f0ec}}
body{{font-family:"Noto Sans JP","Hiragino Kaku Gothic ProN",sans-serif;background:var(--bg);color:var(--text);line-height:1.85;font-size:16px;-webkit-font-smoothing:antialiased}}
a{{color:var(--link);text-decoration:none}}a:hover{{text-decoration:underline}}
.wrap{{max-width:780px;margin:0 auto;padding:0 20px}}
header{{background:#fff;border-bottom:1px solid var(--border);padding:18px 0}}header .wrap{{display:flex;align-items:center;justify-content:space-between}}.site-name{{font-size:14px;font-weight:700;color:var(--accent);letter-spacing:.5px}}
.site-nav{{display:flex;gap:16px}}.site-nav a{{font-size:12px;color:var(--text-sub);text-decoration:none;padding:3px 10px;background:var(--tag-bg);border-radius:20px}}.site-nav a:hover{{color:var(--accent);text-decoration:none}}
nav.breadcrumb{{font-size:13px;color:var(--text-sub);padding:12px 0;border-bottom:1px solid var(--border);background:#fff}}nav.breadcrumb a{{color:var(--text-sub)}}
.hero{{background:linear-gradient(135deg,#34495e 0%,#2c3e50 100%);color:#fff;padding:56px 0 48px;text-align:center}}.hero h1{{font-size:24px;line-height:1.5;font-weight:700;letter-spacing:.5px}}
main{{padding:48px 0 64px}}main h2{{font-size:20px;font-weight:700;color:var(--accent);margin:48px 0 20px;padding-bottom:10px;border-bottom:2px solid var(--accent)}}main h2:first-of-type{{margin-top:0}}main h3{{font-size:17px;font-weight:700;margin:32px 0 12px;padding-left:14px;border-left:4px solid var(--accent)}}main p{{margin-bottom:20px}}main ul,main ol{{margin:0 0 20px 24px}}main li{{margin-bottom:8px;font-size:15px}}
table.compare{{width:100%;border-collapse:collapse;margin:24px 0;font-size:14px}}table.compare th,table.compare td{{border:1px solid var(--border);padding:12px 14px;text-align:left}}table.compare th{{background:var(--accent-light);color:var(--accent);font-weight:700;white-space:nowrap}}table.compare td{{background:#fff}}
.related-terms{{background:var(--accent-light);border-radius:10px;padding:24px 28px;margin:40px 0}}.related-terms h3{{font-size:16px;font-weight:700;color:var(--accent);margin:0 0 12px;padding:0;border:none}}.related-terms ul{{margin:0;list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:10px}}.related-terms li{{margin:0}}.related-terms a{{display:inline-block;padding:6px 14px;font-size:13px;background:var(--card);border:1px solid var(--border);border-radius:20px;color:var(--accent);text-decoration:none}}.related-terms a:hover{{background:var(--accent);color:#fff;border-color:var(--accent);text-decoration:none}}
.related{{margin:40px 0}}.related h3{{font-size:16px;font-weight:700;color:var(--accent);margin:0 0 12px;padding:0;border:none}}.related ul{{list-style:none;padding:0;margin:0}}.related li{{margin-bottom:8px}}.related a{{font-size:14px}}
.author-box{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:24px 28px;margin:40px 0;display:flex;gap:20px;align-items:flex-start}}.author-box .author-icon{{width:64px;height:64px;flex-shrink:0;border-radius:50%;overflow:hidden}}.author-box .author-icon img{{width:100%;height:100%}}.author-box .author-text p{{font-size:14px;color:var(--text-sub);margin-bottom:8px;line-height:1.7}}.author-box .author-text p:last-child{{margin-bottom:0}}.author-box .author-name{{font-weight:700;font-size:15px;color:var(--text);margin-bottom:4px}}
footer{{background:#fff;border-top:1px solid var(--border);padding:32px 0;text-align:center;font-size:13px;color:var(--text-sub)}}
@media(max-width:600px){{.hero h1{{font-size:20px}}main h2{{font-size:18px}}table.compare{{font-size:13px}}table.compare th,table.compare td{{padding:8px 10px}}}}
.footer-links{{margin-bottom:12px}}.footer-links a{{margin:0 12px;color:var(--text-sub);font-size:13px}}.footer-links a:hover{{color:var(--accent)}}
</style>
<link rel="stylesheet" href="/search.css">
<script src="/search.js" defer></script>
</head>
<body>
<header><div class="wrap"><a href="/" class="site-name">ツバサのメモ帳</a><nav class="site-nav"><a href="/archive.html">記事一覧</a><a href="/glossary/">用語集</a></nav></div></header>
<div class="site-search-wrap"><div class="wrap"><input type="search" id="site-search-input" placeholder="サービス名・キーワードで検索" autocomplete="off" aria-label="サイト内検索"><div id="site-search-results" hidden></div></div></div>
<nav class="breadcrumb"><div class="wrap"><a href="/">トップ</a> &gt; <a href="/glossary/">用語集</a> &gt; {breadcrumb_label}</div></nav>
<section class="hero"><div class="wrap"><h1>{h1}</h1></div></section>
<main><div class="wrap">
{body}
{related_terms_html}
{related_articles_html}
<div class="author-box"><div class="author-icon"><img src="/icons/tsubasa.png" alt="ツバサ" width="64" height="64"></div><div class="author-text"><p class="author-name">ツバサ</p><p>EC関係の仕事をしています。このサイトは自分が調べたことの備忘録です。Photoshopは少し使えますが苦手で、ちょっとした画像補正はもっぱらスマホアプリ派。アプリで対応しきれない本格的なレタッチはプロに依頼しています。</p></div></div>
</div></main>
<footer><div class="wrap"><div class="footer-links"><a href="privacy-policy.html">プライバシーポリシー</a><a href="contact.html">お問い合わせ</a><a href="about.html">運営者情報</a></div>&copy; 2026 ツバサのメモ帳</div></footer>
</body></html>'''


def make_jsonld(faqs):
    if not faqs:
        return ''
    entities = []
    for q, a in faqs:
        entities.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join(entities) + ']}\n</script>'


def make_related_terms(terms):
    if not terms:
        return ''
    items = ''.join(f'<li><a href="{slug}.html">{label}</a></li>' for slug, label in terms)
    return f'<div class="related-terms"><h3>関連する用語</h3><ul>{items}</ul></div>'


def make_related_articles(articles):
    if not articles:
        return ''
    items = ''.join(f'<li><a href="/{slug}">{label}</a></li>' for slug, label in articles)
    return f'<div class="related"><h3>関連する記事</h3><ul>{items}</ul></div>'


# ============================================================
# 20用語のデータ定義
# ============================================================

TERMS = [
# --- 1. CTR ---
{
  'slug': 'ctr',
  'title': 'CTR（クリック率）とは？検索結果で見るべき数字の話｜ツバサのメモ帳',
  'meta_desc': 'CTR（Click Through Rate）は表示回数に対するクリック数の割合。Google検索結果でのCTRの計算方法・平均値の目安・Search ConsoleでのCTR確認手順をEC担当の視点でまとめた。',
  'keywords': 'CTR とは,クリック率 計算,検索結果 CTR 平均,CTR 改善',
  'og_desc': 'CTR（クリック率）の意味・計算方法・改善のポイントをまとめた備忘録。',
  'breadcrumb_label': 'CTR（クリック率）',
  'h1': 'CTR（クリック率）とは？<br>検索結果で見るべき数字の話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>Google Search Consoleを見ていると「CTR」という列がある。表示回数やクリック数は直感的にわかるが、CTRが何を意味していて、どのくらいあれば良いのか最初はわからなかったので調べた。</p>

<h2>CTR（クリック率）とは</h2>
<p>CTRはClick Through Rateの略で、「表示された回数のうち、何回クリックされたか」を示す割合だ。計算式は「クリック数 ÷ 表示回数 × 100（%）」。たとえば検索結果に1,000回表示されて10回クリックされたらCTRは1%になる。</p>
<p>Google検索の場合、掲載順位1位のCTRは一般的に25〜35%程度、10位になると2〜3%程度まで下がるとされている。順位が低いほどCTRは下がるが、同じ順位でもタイトルやmeta descriptionの内容によって差が出る。</p>

<h2>ブログ運営で出てくる場面</h2>
<h3>Search ConsoleでCTRを確認する</h3>
<p>Google Search Consoleの「検索パフォーマンス」レポートで、ページごと・クエリごとのCTRが確認できる。表示回数が多いのにCTRが低いページは、検索結果でユーザーに「読みたい」と思われていない可能性がある。</p>
<h3>タイトルを変えてCTRが動くか確認する</h3>
<p>CTRが低いページのタイトルやmeta descriptionを書き直し、1〜2週間後にCTRが改善したか確認するのがよくある改善手順だ。順位を上げるのは難しくても、タイトルの工夫でCTRを上げることは比較的やりやすい。</p>

<h2>覚えておきたいポイント</h2>
<h3>CTRとCVRは別の指標</h3>
<p>CTRは「クリックされた割合」、CVRは「成果（購入など）に至った割合」。CTRは検索結果やバナー広告などの「入り口」の評価、CVRはサイトに入ってからの「出口」の評価だ。</p>
<h3>表示回数が少ないとCTRは参考にならない</h3>
<p>表示回数が10回でクリック1回ならCTR10%になるが、母数が少なすぎて信頼できない。最低でも数百回以上の表示回数があるページで見るのが現実的だ。</p>''',
  'faqs': [
    ('CTR（クリック率）とは何ですか？', 'CTRはClick Through Rateの略で、表示回数に対するクリック数の割合です。計算式は「クリック数÷表示回数×100（%）」で、検索結果や広告の効果を測る指標として使われます。'),
    ('Google検索のCTR平均はどのくらいですか？', '検索順位1位で25〜35%程度、5位で5〜8%程度、10位で2〜3%程度が一般的な目安です。ただしクエリの種類やタイトルの内容によって大きく変わります。'),
    ('CTRを改善するにはどうすればよいですか？', 'まずはtitleタグとmeta descriptionの見直しが効果的です。検索意図に合ったタイトルにする、具体的な数字を入れる、ユーザーの悩みに直接答える表現にするなどの方法があります。'),
    ('CTRとCVRの違いは何ですか？', 'CTRは検索結果や広告が表示された回数に対するクリック率、CVRはサイト訪問者のうち購入などの成果に至った割合です。CTRは流入の質、CVRはサイト内の成果を測ります。'),
    ('CTRはどこで確認できますか？', 'Google Search Consoleの「検索パフォーマンス」で確認できます。ページ別・クエリ別にCTRが表示され、表示回数やクリック数と合わせて分析できます。'),
  ],
  'related_terms': [('cvr', 'CVR'), ('impression', '表示回数'), ('cpa', 'CPA'), ('long-tail', 'ロングテール')],
  'related_articles': [('search-console-basics.html', 'サーチコンソールの見方を覚えた備忘録'), ('search-console-ctr.html', '記事のタイトルを変えたらCTRが動いた話')],
},

# --- 2. meta description ---
{
  'slug': 'meta-description',
  'title': 'meta descriptionとは？検索結果の説明文を自分で設定する話｜ツバサのメモ帳',
  'meta_desc': 'meta descriptionはHTMLのheadタグに書く検索結果の説明文。Googleが検索結果に表示するスニペットの候補になる。書き方のコツと最適な文字数をまとめた備忘録。',
  'keywords': 'meta description とは,メタディスクリプション 書き方,meta description 文字数,検索結果 説明文',
  'og_desc': 'meta descriptionの役割と書き方をまとめた備忘録。',
  'breadcrumb_label': 'meta description',
  'h1': 'meta descriptionとは？<br>検索結果の説明文を自分で設定する話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>ブログを始めたとき、検索結果に表示される説明文がページ内の文章を適当に切り取ったものになっていた。調べてみたらmeta descriptionというタグを自分で書けば、この説明文をコントロールできると知った。</p>

<h2>meta descriptionとは</h2>
<p>HTMLの&lt;head&gt;タグ内に記述するメタタグの一つで、そのページの概要を検索エンジンやSNSに伝えるためのものだ。書き方は<code>&lt;meta name="description" content="ここに説明文"&gt;</code>のようになる。</p>
<p>Googleの検索結果にページが表示されるとき、タイトルの下に出る説明文（スニペット）の候補になる。ただしGoogleがmeta descriptionをそのまま使うとは限らず、ページ内容から自動生成されることもある。</p>

<h2>書くときに意識していること</h2>
<h3>文字数は110〜125文字程度</h3>
<p>PCの検索結果で表示される文字数は120文字前後。長すぎると途中で切れ、短すぎると情報が不足する。このブログでは110〜125文字を目安にしている。</p>
<h3>ページの結論を先に書く</h3>
<p>「この記事では〜をまとめました」のように何が書いてあるかを冒頭に置く。検索結果をスクロールしているユーザーが「自分の知りたいことが書いてありそうだ」と判断する材料になる。</p>

<h2>覚えておきたいポイント</h2>
<h3>meta descriptionは直接の順位要因ではない</h3>
<p>Googleはmeta descriptionをランキング要因として使っていないと公式に述べている。ただしCTR（クリック率）に影響するため、間接的にSEOに効く場面はある。</p>
<h3>全ページに固有の説明文を書く</h3>
<p>同じ説明文を複数ページに使い回すと、Googleに「重複コンテンツ」と判断される可能性がある。面倒でもページごとに固有の内容を書いた方がよい。</p>''',
  'faqs': [
    ('meta descriptionとは何ですか？', 'HTMLのheadタグに記述するメタタグで、ページの概要を説明する文章です。Googleの検索結果でタイトルの下に表示されるスニペットの候補になります。'),
    ('meta descriptionの最適な文字数は？', 'PC検索結果では120文字前後が表示されるため、110〜125文字程度が目安です。スマホではもう少し短く表示されることもあります。'),
    ('meta descriptionはSEOに影響しますか？', 'Googleは直接のランキング要因としては使っていないと明言しています。ただしCTR（クリック率）に影響するため、間接的にSEOに効果がある場合があります。'),
    ('meta descriptionを書かないとどうなりますか？', 'Googleがページ本文から自動的にスニペットを生成します。意図しない文章が表示されることがあるため、自分で書いておくことをおすすめします。'),
    ('meta descriptionにキーワードを入れるべきですか？', '検索クエリと一致する語句がmeta descriptionに含まれていると太字で表示されるため、自然な形で含めるのが効果的です。ただしキーワードを詰め込みすぎると不自然になります。'),
  ],
  'related_terms': [('ctr', 'CTR'), ('ogp-image', 'OGP画像'), ('alt-attribute', 'alt属性'), ('first-view', 'ファーストビュー')],
  'related_articles': [('blog-seo-basics.html', '個人ブログのSEOを勉強した記録'), ('search-console-ctr.html', '記事のタイトルを変えたらCTRが動いた話')],
},

# --- 3. canonical ---
{
  'slug': 'canonical',
  'title': 'canonical（カノニカル）とは？URLの正規化で重複を防ぐ話｜ツバサのメモ帳',
  'meta_desc': 'canonical（カノニカル）はHTMLで正規URLを指定するタグ。同じ内容のページが複数のURLでアクセスできるとき、検索エンジンにどのURLを評価してほしいかを伝える仕組みをまとめた。',
  'keywords': 'canonical とは,カノニカルURL,link rel canonical,URL正規化,重複コンテンツ対策',
  'og_desc': 'canonicalタグの役割と設定方法をまとめた備忘録。',
  'breadcrumb_label': 'canonical',
  'h1': 'canonical（カノニカル）とは？<br>URLの正規化で重複を防ぐ話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>ブログのHTMLテンプレートを作ってもらったとき、headタグの中に<code>&lt;link rel="canonical"&gt;</code>という見慣れない記述があった。何のためのタグか調べたのでメモしておく。</p>

<h2>canonicalとは</h2>
<p>canonicalタグは、「このページの正規URLはこれです」と検索エンジンに伝えるためのHTMLタグだ。書き方は<code>&lt;link rel="canonical" href="https://example.com/page.html"&gt;</code>。</p>
<p>同じ内容のページが複数のURLでアクセスできてしまうケースがある。たとえばURLにパラメータがついた場合（?ref=twitterなど）、httpとhttpsの両方でアクセスできる場合、www有無の違いなどだ。こういうとき、Googleがどちらを「本物」として評価すべきか迷わないよう、正規のURLを教えてあげるのがcanonicalタグの役割になる。</p>

<h2>このブログでの使い方</h2>
<h3>全ページにcanonicalを設置</h3>
<p>このブログでは全ページのheadタグにcanonicalタグを入れている。自分自身のURLを指定する形で、「このURLが正です」と明示している。重複が発生していなくても、念のため設置しておくのが一般的だ。</p>
<h3>リダイレクトページでの指定</h3>
<p>ページを移転したとき、旧URLにcanonicalタグで新URLを指定すると、検索エンジンに「評価は新URLに集約してほしい」と伝えられる。meta refreshによるリダイレクトと組み合わせて使うことがある。</p>

<h2>覚えておきたいポイント</h2>
<h3>canonicalは「指示」ではなく「ヒント」</h3>
<p>Googleはcanonicalタグを絶対的な指示ではなくヒントとして扱う。ページ内容が大きく異なるのに同じcanonicalを指定するなど、不適切な使い方をするとGoogleが無視することもある。</p>
<h3>自己参照canonicalでも設置する意味がある</h3>
<p>自分自身のURLを指すcanonicalタグでも、パラメータ付きURLや大文字小文字違いのURLからのアクセスを正規化できるため、設置しておくのが安全だ。</p>''',
  'faqs': [
    ('canonicalタグとは何ですか？', 'HTMLのheadタグに記述するlink要素で、ページの正規URLを検索エンジンに伝えるためのタグです。重複コンテンツの問題を防ぐために使われます。'),
    ('canonicalタグを設置しないとどうなりますか？', '同じ内容のページが複数URLに存在すると、Googleが評価を分散させてしまう可能性があります。検索順位に悪影響が出ることがあります。'),
    ('canonicalと301リダイレクトの違いは？', '301リダイレクトはユーザーを別URLに転送します。canonicalはユーザーはそのまま閲覧でき、検索エンジンにだけ正規URLを伝えます。ページが完全に移転した場合は301、両方のURLを残したい場合はcanonicalが適しています。'),
    ('自分自身を指すcanonicalに意味はありますか？', 'あります。URLパラメータが付いたアクセスやwww有無の違いを正規化できるため、自己参照canonicalでも設置しておくことが推奨されています。'),
    ('canonicalタグはGoogleに必ず従ってもらえますか？', 'いいえ。Googleはcanonicalをヒントとして扱い、最終的な判断はGoogle側が行います。ページ内容と矛盾する指定は無視されることがあります。'),
  ],
  'related_terms': [('redirect', 'リダイレクト'), ('nofollow', 'nofollow'), ('sitemap', 'サイトマップ')],
  'related_articles': [('blog-seo-basics.html', '個人ブログのSEOを勉強した記録'), ('google-index-not-found.html', 'Googleにインデックスされるまで')],
},

# --- 4〜20: 残りの用語 ---
# 以下、同じ構造でデータを定義
]

# --- 4. JSON-LD ---
TERMS.append({
  'slug': 'json-ld', 'title': 'JSON-LDとは？構造化データで検索結果を変える話｜ツバサのメモ帳',
  'meta_desc': 'JSON-LDはGoogleの検索結果にFAQやパンくずリストなどのリッチリザルトを表示させるための構造化データ形式。HTMLのscriptタグに記述する書き方と、ブログでの活用方法をまとめた。',
  'keywords': 'JSON-LD とは,構造化データ 書き方,FAQPage JSON-LD,リッチリザルト', 'og_desc': 'JSON-LDの役割と書き方をまとめた備忘録。',
  'breadcrumb_label': 'JSON-LD', 'h1': 'JSON-LDとは？<br>構造化データで検索結果を変える話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>ブログにFAQセクションを追加したとき、「JSON-LDで構造化データを書くと検索結果にFAQが表示されることがある」と知った。最初は何のことかさっぱりだったが、調べてみたら意外と単純な仕組みだった。</p>
<h2>JSON-LDとは</h2>
<p>JSON-LD（JSON for Linking Data）は、Webページの情報を検索エンジンに構造的に伝えるためのデータ形式だ。HTMLの&lt;script type="application/ld+json"&gt;タグ内にJSON形式で記述する。</p>
<p>たとえばFAQの質問と回答をJSON-LDで書いておくと、Google検索結果にFAQのアコーディオンが表示される（リッチリザルト）ことがある。ページの内容自体は変わらないが、検索結果での見た目が変わる。</p>
<h2>このブログでの使い方</h2>
<h3>FAQPage構造化データ</h3>
<p>このブログでは各記事にFAQセクションを設け、同じ内容をJSON-LDのFAQPage形式でも記述している。質問と回答のペアを最低5組は入れるようにしている。</p>
<h3>記述する場所</h3>
<p>headタグ内にscriptタグで記述する。本文のHTMLには影響しないので、既存ページに後から追加しても表示が崩れることはない。</p>
<h2>覚えておきたいポイント</h2>
<h3>リッチリザルトが表示されるとは限らない</h3>
<p>JSON-LDを正しく書いてもGoogleがリッチリザルトを表示するかどうかはGoogle次第だ。ただし構造化データがあればAIがページの内容を理解しやすくなるため、LLMO的にもメリットがある。</p>
<h3>Googleのリッチリザルトテストで検証できる</h3>
<p>Googleが提供するリッチリザルトテストツールにURLを入れると、構造化データが正しく記述されているか確認できる。新しいページを公開する前にチェックしておくと安心だ。</p>''',
  'faqs': [
    ('JSON-LDとは何ですか？','JSON-LDはJSON for Linking Dataの略で、Webページの情報を検索エンジンに構造的に伝えるためのデータ形式です。HTMLのscriptタグ内に記述します。'),
    ('JSON-LDを書くと何が変わりますか？','Google検索結果にFAQやパンくずリストなどのリッチリザルトが表示される可能性があります。また、AIがページ内容を理解しやすくなります。'),
    ('JSON-LDはどこに書きますか？','HTMLのhead内に&lt;script type=&quot;application/ld+json&quot;&gt;タグで記述します。本文のHTMLとは独立しているため、既存ページに後から追加できます。'),
    ('JSON-LDとMicrodataの違いは？','JSON-LDはscriptタグ内に独立して記述します。MicrodataはHTML要素に属性を追加する形式です。Googleは公式にJSON-LDを推奨しています。'),
    ('構造化データが正しいか確認する方法は？','GoogleのリッチリザルトテストツールにページのURLを入力すると、構造化データの検証ができます。エラーがあれば具体的に指摘してくれます。'),
  ],
  'related_terms': [('meta-description', 'meta description'), ('breadcrumb', 'パンくずリスト')],
  'related_articles': [('faq-structured-data.html', 'FAQ構造化データを設置した記録'), ('llmo-article-writing.html', 'AIに引用されやすい記事の書き方')],
})

# --- 5. sitemap ---
TERMS.append({
  'slug': 'sitemap', 'title': 'サイトマップ（sitemap.xml）とは？Googleに全ページを教える話｜ツバサのメモ帳',
  'meta_desc': 'sitemap.xmlはサイト内の全ページ一覧をXML形式で記述し、検索エンジンに送信するファイル。Google Search Consoleへの送信方法とサイトマップの書き方をまとめた。',
  'keywords': 'サイトマップ とは,sitemap.xml 書き方,Google サイトマップ送信,XML サイトマップ', 'og_desc': 'sitemap.xmlの役割と書き方をまとめた備忘録。',
  'breadcrumb_label': 'サイトマップ', 'h1': 'サイトマップ（sitemap.xml）とは？<br>Googleに全ページを教える話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>ブログを始めて数週間経っても、Googleに記事が全然表示されなかった。調べたらsitemap.xmlをGoogle Search Consoleに送信していなかったのが原因だった。</p>
<h2>サイトマップとは</h2>
<p>sitemap.xmlは、サイト内にある全ページのURLを一覧にしたXML形式のファイルだ。このファイルをGoogle Search Consoleに送信すると、Googleのクローラー（ページを巡回するロボット）が「このサイトにはこんなページがある」と把握しやすくなる。</p>
<p>サイトマップがなくてもGoogleはリンクをたどってページを見つけることはできるが、新規サイトやページ数が多いサイトでは発見が遅れることがある。サイトマップを送信しておけば、この遅れをある程度短縮できる。</p>
<h2>このブログでの使い方</h2>
<h3>記事追加のたびに更新する</h3>
<p>新しい記事を公開するたびに、sitemap.xmlに新しいURLを追加している。サイトマップに載っていないページはGoogleに発見されにくいため、この更新を忘れるとインデックスが遅れる。</p>
<h3>Search Consoleで送信状態を確認する</h3>
<p>Google Search Consoleの「サイトマップ」メニューで、送信したサイトマップが正しく読み取られているか確認できる。エラーが出ていたら修正が必要だ。</p>
<h2>覚えておきたいポイント</h2>
<h3>サイトマップに載せたページが必ずインデックスされるわけではない</h3>
<p>サイトマップは「このページがあります」という通知であり、インデックスの保証ではない。ページの内容が薄かったり、品質が低いとGoogleがインデックスしない判断をすることもある。</p>
<h3>lastmodの日付を正確に書く</h3>
<p>各URLに設定するlastmod（最終更新日）は、実際にページを更新した日付にする。毎日全ページの日付を更新するような行為はGoogleからの信頼を失う原因になる。</p>''',
  'faqs': [
    ('sitemap.xmlとは何ですか？','サイト内の全ページURLをXML形式で記述したファイルです。Google Search Consoleに送信すると、クローラーがページを発見しやすくなります。'),
    ('サイトマップがないとGoogleに表示されませんか？','表示されないわけではありませんが、新規サイトやページ数が多いサイトでは発見が遅れることがあります。送信しておくことを推奨します。'),
    ('サイトマップはどうやって作りますか？','XMLの仕様に従って手動で書くか、静的サイトジェネレーターやプラグインで自動生成できます。このブログではPythonスクリプトで生成しています。'),
    ('サイトマップはどこに置きますか？','サイトのルートディレクトリ（https://example.com/sitemap.xml）に配置するのが一般的です。robots.txtにサイトマップのURLを記述しておくと、クローラーが自動的に見つけます。'),
    ('サイトマップの更新頻度は？','ページを追加・更新したタイミングで更新するのが理想的です。変更がないのに頻繁に更新してもメリットはありません。'),
  ],
  'related_terms': [('robots-txt', 'robots.txt'), ('index-registration', 'インデックス登録'), ('canonical', 'canonical')],
  'related_articles': [('google-index-not-found.html', 'Googleにインデックスされるまで'), ('blog-seo-basics.html', '個人ブログのSEOを勉強した記録')],
})

# --- 6. robots.txt ---
TERMS.append({
  'slug': 'robots-txt', 'title': 'robots.txtとは？クローラーに見せる範囲を指定する話｜ツバサのメモ帳',
  'meta_desc': 'robots.txtはサイトのルートに置くテキストファイルで、検索エンジンのクローラーにアクセスしてよい範囲を指示する。書き方とsitemap.xmlの記述方法をまとめた。',
  'keywords': 'robots.txt とは,robots.txt 書き方,クローラー 制御,robots.txt sitemap', 'og_desc': 'robots.txtの役割と書き方をまとめた備忘録。',
  'breadcrumb_label': 'robots.txt', 'h1': 'robots.txtとは？<br>クローラーに見せる範囲を指定する話',
  'body': '''<p>こんにちは、ツバサです。</p>
<p>ブログを作ったとき、AIに「robots.txtも設置しておきましょう」と言われた。名前からしてロボット関連だとは想像できたが、何をするファイルなのか調べた。</p>
<h2>robots.txtとは</h2>
<p>robots.txtは、Webサイトのルートディレクトリに置くテキストファイルで、検索エンジンのクローラー（自動巡回プログラム）に対して「このディレクトリは見に来なくていい」「ここは巡回してOK」と指示するものだ。</p>
<p>たとえば管理用のページや下書きフォルダをクローラーに見せたくない場合に使う。ただしrobots.txtはあくまで「お願い」であり、悪意のあるボットが従う保証はない。</p>
<h2>このブログでの使い方</h2>
<h3>全ページ巡回OK + サイトマップ記載</h3>
<p>このブログでは特に隠すページがないため、robots.txtにはクローラーの巡回を全許可する記述と、サイトマップのURLを記載している。クローラーがrobots.txtを最初に読み、そこからサイトマップを見つけるという流れになる。</p>
<h2>覚えておきたいポイント</h2>
<h3>robots.txtでブロックしてもインデックスされることがある</h3>
<p>robots.txtでクローラーのアクセスをブロックしても、他サイトからのリンクなどでURLを知ったGoogleがインデックスしてしまうことがある。確実にインデックスさせたくない場合はnoindexメタタグも併用する必要がある。</p>
<h3>robots.txtの記述ミスに注意</h3>
<p>Disallow（拒否）の記述を間違えると、サイト全体がクローラーから遮断されてしまう。Search Consoleの「robots.txtテスター」で記述が正しいか確認してから公開するのが安全だ。</p>''',
  'faqs': [
    ('robots.txtとは何ですか？','Webサイトのルートに置くテキストファイルで、検索エンジンのクローラーにどのページを巡回してよいか指示するものです。'),
    ('robots.txtは必ず設置する必要がありますか？','必須ではありませんが、設置しておくことが推奨されています。特にサイトマップのURLを記載しておくと、クローラーがサイト構造を把握しやすくなります。'),
    ('robots.txtでブロックするとインデックスされませんか？','必ずしもそうではありません。他サイトからのリンク経由でURLが発見され、インデックスされることがあります。確実に除外したい場合はnoindexメタタグも併用してください。'),
    ('robots.txtはどこに置きますか？','サイトのルートディレクトリに配置します。URLはhttps://example.com/robots.txtの形になります。'),
    ('robots.txtの記述ミスが心配です。確認方法は？','Google Search Consoleの「robots.txtテスター」機能で、特定のURLがブロックされるかどうかを確認できます。'),
  ],
  'related_terms': [('sitemap', 'サイトマップ'), ('index-registration', 'インデックス登録'), ('nofollow', 'nofollow')],
  'related_articles': [('google-index-not-found.html', 'Googleにインデックスされるまで')],
})

# --- 7. redirect ---
TERMS.append({'slug':'redirect','title':'リダイレクトとは？ページ移転でURLを転送する仕組み｜ツバサのメモ帳','meta_desc':'リダイレクトはURLを別のURLに自動転送する仕組み。301（恒久的転送）と302（一時的転送）の違い、HTMLのmeta refreshでの実装方法をまとめた。','keywords':'リダイレクト とは,301リダイレクト,302リダイレクト,meta refresh,URL転送','og_desc':'リダイレクトの種類と使い分けをまとめた備忘録。','breadcrumb_label':'リダイレクト','h1':'リダイレクトとは？<br>ページ移転でURLを転送する仕組み',
'body':'''<p>こんにちは、ツバサです。</p>
<p>記事のURLを変更したとき、古いURLにアクセスした人を新しいURLに自動で飛ばす方法を調べた。これがリダイレクトだ。</p>
<h2>リダイレクトとは</h2>
<p>あるURLにアクセスしたとき、自動的に別のURLに転送する仕組みのこと。ページのURLを変更したり、サイトを引っ越したりしたときに、旧URLへの訪問者を新URLに誘導するために使う。</p>
<p>代表的な種類は301リダイレクト（恒久的な移転）と302リダイレクト（一時的な移転）の2つ。301の場合、検索エンジンは旧URLの評価を新URLに引き継ぐ。302は一時的な転送なので評価の引き継ぎは行われない。</p>
<h2>静的サイトでの実装方法</h2>
<h3>meta refreshタグを使う</h3>
<p>GitHub Pagesのような静的サイトではサーバー設定ができないため、HTMLのmeta refreshタグでリダイレクトする。<code>&lt;meta http-equiv="refresh" content="0;url=新URL"&gt;</code>と書くと、ページを開いた瞬間に新URLに転送される。</p>
<h3>canonicalタグも併記する</h3>
<p>meta refreshだけでは検索エンジンが「恒久的な移転」と判断しないことがある。canonicalタグで新URLを指定し、noindexも設定しておくのが安全だ。</p>
<h2>覚えておきたいポイント</h2>
<h3>リダイレクトチェーンを作らない</h3>
<p>A→B→Cのように転送が連鎖すると、ページの読み込みが遅くなり、検索エンジンの評価にも悪影響が出る。転送は1回で完結するようにする。</p>''',
'faqs':[('リダイレクトとは何ですか？','あるURLにアクセスしたとき、自動的に別のURLに転送する仕組みです。ページのURL変更やサイト移転時に、訪問者とGoogleの評価を新URLに引き継ぐために使います。'),('301と302リダイレクトの違いは？','301は恒久的な移転で検索エンジンの評価が新URLに引き継がれます。302は一時的な転送で評価の引き継ぎは行われません。ページを完全に移動した場合は301を使います。'),('静的サイトでリダイレクトするには？','HTMLのmeta refreshタグを使います。サーバー設定が不要なため、GitHub Pagesなどの静的ホスティングでも実装できます。'),('リダイレクトは何秒で転送すべきですか？','meta refreshのcontent属性を0にすると即座に転送されます。ユーザーに旧ページを見せる必要がなければ0秒が推奨です。'),('リダイレクトチェーンとは何ですか？','A→B→Cのようにリダイレクトが連鎖することです。読み込み速度の低下やSEO評価の分散を招くため、転送は1回で完結させるのが望ましいです。')],
'related_terms':[('canonical','canonical'),('nofollow','nofollow'),('index-registration','インデックス登録')],
'related_articles':[('google-index-not-found.html','Googleにインデックスされるまで')],
})

# --- 8. Exif ---
TERMS.append({'slug':'exif','title':'Exif（イグジフ）とは？写真に埋め込まれた撮影情報の話｜ツバサのメモ帳','meta_desc':'Exifは写真ファイルに自動記録される撮影情報。カメラ機種・撮影日時・GPS位置情報などが含まれる。SNS投稿時の注意点と確認・削除方法をまとめた。','keywords':'Exif とは,Exif情報 確認,写真 位置情報,Exif 削除方法','og_desc':'Exif情報の中身と確認・削除方法をまとめた備忘録。','breadcrumb_label':'Exif','h1':'Exif（イグジフ）とは？<br>写真に埋め込まれた撮影情報の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>スマホで撮った写真をSNSに投稿するとき「位置情報が含まれています」と表示されてドキッとした経験がある。この位置情報が入っているのがExifだ。</p>
<h2>Exifとは</h2>
<p>Exif（Exchangeable Image File Format）は、デジタルカメラやスマートフォンが写真撮影時に自動的に記録するメタデータの規格だ。撮影日時、カメラの機種名、シャッタースピード、絞り値、ISO感度、そしてGPSが有効な場合は位置情報（緯度・経度）が含まれる。</p>
<p>写真ファイル（JPEGなど）の中に埋め込まれているため、ファイルを送信・共有するとExif情報もそのまま相手に渡る場合がある。</p>
<h2>SNS投稿時の注意点</h2>
<h3>主要SNSは自動削除してくれる</h3>
<p>X（旧Twitter）、Instagram、LINEは写真をアップロードする際にExif情報を自動的に削除する仕様になっている。そのため、これらのSNSに投稿した写真から位置情報が第三者に見られる心配は基本的にない。</p>
<h3>メールやクラウド共有は要注意</h3>
<p>メール添付やGoogle Drive、Dropboxでの共有ではExif情報がそのまま残る。自宅で撮った写真をメールで送ると、自宅の緯度経度が相手に伝わる可能性がある。</p>
<h2>覚えておきたいポイント</h2>
<h3>スマホの位置情報設定を確認しておく</h3>
<p>iPhoneは「設定」→「プライバシー」→「位置情報サービス」→「カメラ」、Androidは「カメラアプリの設定」→「位置情報タグ」で、撮影時のGPS記録をオン/オフできる。</p>''',
'faqs':[('Exifとは何ですか？','Exchangeable Image File Formatの略で、デジタル写真に自動記録される撮影情報です。カメラ機種、撮影日時、GPS位置情報などが含まれます。'),('SNSに写真を投稿するとExifは残りますか？','X、Instagram、LINEは投稿時にExif情報を自動削除します。ただしメール添付やクラウドストレージでの共有ではExifがそのまま残ります。'),('Exif情報を確認する方法は？','iPhoneは「写真」アプリで詳細情報を表示、Windowsはファイルを右クリック→プロパティ→詳細タブで確認できます。'),('Exif情報を削除する方法は？','iPhoneは「写真」アプリで位置情報を削除できます。Windowsはプロパティの詳細タブから個人情報を削除できます。専用アプリを使う方法もあります。'),('EC商品写真にもExifは含まれますか？','はい。カメラで撮影した商品写真にもExif情報が含まれます。ECサイトにアップロードする際は、プラットフォームがExifを削除してくれることが多いですが、事前に確認しておくと安心です。')],
'related_terms':[('heif-heic','HEIF/HEIC'),('png','PNG'),('webp','WebP')],
'related_articles':[('exif-info.html','写真のExif位置情報を確認・削除する方法')],
})

# --- 9. breadcrumb ---
TERMS.append({'slug':'breadcrumb','title':'パンくずリストとは？サイト内の現在地を示すナビゲーション｜ツバサのメモ帳','meta_desc':'パンくずリスト（breadcrumb）はWebページの階層構造を示すナビゲーション。ユーザーが今サイトのどこにいるかを視覚的に伝え、SEOにも効果がある仕組みをまとめた。','keywords':'パンくずリスト とは,breadcrumb SEO,パンくず ナビゲーション,構造化データ パンくず','og_desc':'パンくずリストの役割とSEO効果をまとめた備忘録。','breadcrumb_label':'パンくずリスト','h1':'パンくずリストとは？<br>サイト内の現在地を示すナビゲーション',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログのテンプレートを作るときに「パンくずリストも入れておきましょう」とAIに言われた。ヘンゼルとグレーテルのパンくずが由来だと知って少し面白かった。</p>
<h2>パンくずリストとは</h2>
<p>Webサイトのページ上部などに表示される「トップ ＞ 用語集 ＞ パンくずリスト」のような階層ナビゲーションのこと。英語ではbreadcrumb（パンくず）と呼ぶ。ユーザーが今サイトのどの階層にいるのかを視覚的に伝え、上位の階層にワンクリックで戻れる機能を持つ。</p>
<h2>ブログでの役割</h2>
<h3>ユーザビリティの向上</h3>
<p>検索エンジン経由で個別記事に直接たどり着いたユーザーが、サイトの他のページを回遊しやすくなる。「トップ」や「記事一覧」にすぐ戻れるのは地味だが便利だ。</p>
<h3>SEOへの効果</h3>
<p>パンくずリストはサイトの階層構造をGoogleに伝える役割もある。JSON-LDで構造化データとして記述すると、検索結果にパンくずが表示されることがあり、クリック率の改善につながる。</p>
<h2>覚えておきたいポイント</h2>
<h3>パンくずリストは内部リンクでもある</h3>
<p>パンくずリストの各階層はリンクになっているため、内部リンクとしても機能する。カテゴリページやトップページへのリンクが全記事から張られることになり、SEO的にも有利だ。</p>''',
'faqs':[('パンくずリストとは何ですか？','Webページの上部に表示される「トップ > カテゴリ > 記事名」のような階層ナビゲーションです。ユーザーが現在地を把握し、上位ページに戻りやすくなります。'),('パンくずリストはSEOに効果がありますか？','あります。サイトの階層構造をGoogleに伝える役割があり、構造化データとして記述すると検索結果にパンくずが表示されることもあります。'),('パンくずリストはどこに設置しますか？','一般的にはページの上部、ヘッダーの直下に設置します。ユーザーが最初に目にする位置に置くことで、サイト内のナビゲーションに役立ちます。'),('パンくずリストの構造化データは必要ですか？','必須ではありませんが、JSON-LDでBreadcrumbList構造化データを記述すると、検索結果にパンくずが表示されやすくなります。'),('パンくずリストがないとSEOに不利ですか？','パンくずリストがないこと自体はペナルティにはなりませんが、内部リンク構造とユーザビリティの面でメリットがあるため、設置が推奨されます。')],
'related_terms':[('json-ld','JSON-LD'),('sitemap','サイトマップ'),('landing-page','ランディングページ')],
'related_articles':[('internal-link-seo.html','内部リンクの貼り方を個人ブログで試した記録')],
})

# --- 10. nofollow ---
TERMS.append({'slug':'nofollow','title':'nofollowとは？外部リンクの評価を渡さないrel属性の話｜ツバサのメモ帳','meta_desc':'nofollowはHTMLのリンクに付与するrel属性で、リンク先にページ評価を渡さないことを検索エンジンに伝える。dofollow・sponsored・ugcとの違いと使い分けをまとめた。','keywords':'nofollow とは,rel nofollow,dofollow 違い,sponsored ugc,外部リンク SEO','og_desc':'nofollowの役割とdofollow・sponsored・ugcとの違いをまとめた備忘録。','breadcrumb_label':'nofollow','h1':'nofollowとは？<br>外部リンクの評価を渡さないrel属性の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログの外部リンクを整理していたとき、「nofollowを付けるべきリンク」と「付けなくてよいリンク」の判断に迷ったので調べた。</p>
<h2>nofollowとは</h2>
<p>HTMLのaタグに<code>rel="nofollow"</code>を付けると、そのリンク先に自分のページの評価（PageRank）を渡さないことを検索エンジンに伝えられる。もともとはスパムコメント対策として導入された属性だが、現在は広告リンクやアフィリエイトリンクにも使われている。</p>
<h2>nofollow・dofollow・sponsored・ugcの違い</h2>
<h3>dofollow（通常リンク）</h3>
<p>何もrel属性を指定しないリンクはdofollowとして扱われ、リンク先にページ評価が渡る。信頼できる公式サイトや参考記事へのリンクはdofollowでよい。</p>
<h3>nofollow</h3>
<p>リンク先に評価を渡したくないときに使う。Googleは2019年以降nofollowを「指示」ではなく「ヒント」として扱うようになったが、意図を伝える手段として引き続き有効だ。</p>
<h3>sponsored</h3>
<p>広告やアフィリエイトなど、金銭が絡むリンクに使う。<code>rel="nofollow sponsored"</code>のように併記するのが一般的。</p>
<h3>ugc</h3>
<p>ユーザー生成コンテンツ（コメント欄など）のリンクに使う。個人ブログではあまり使う場面がない。</p>
<h2>覚えておきたいポイント</h2>
<h3>迷ったらnofollowを付けておく</h3>
<p>外部サイトへのリンクにnofollowを付けても、自分のSEOにマイナスはない。付け忘れて問題のあるサイトに評価を渡してしまう方がリスクがある。</p>''',
'faqs':[('nofollowとは何ですか？','HTMLリンクに付与するrel属性で、リンク先にページ評価を渡さないことを検索エンジンに伝えるものです。広告リンクやアフィリエイトリンクに使います。'),('nofollowとdofollowの違いは？','dofollowはリンク先にページ評価を渡す通常のリンクです。nofollowは評価を渡さないリンクです。信頼できるサイトへはdofollow、広告等はnofollowが一般的です。'),('sponsoredとnofollowの違いは？','sponsoredは広告やアフィリエイトなど金銭が絡むリンク専用の属性です。nofollowと併用して rel=&quot;nofollow sponsored&quot; と書くのが一般的です。'),('nofollowを付け忘れるとどうなりますか？','直ちにペナルティを受けるわけではありませんが、広告リンクにnofollowを付けないとGoogleのガイドライン違反と見なされる可能性があります。'),('内部リンクにもnofollowを付けるべきですか？','通常は不要です。nofollowは主に外部リンクに使うものです。内部リンクに付けると、自サイト内のPageRank循環を妨げてしまいます。')],
'related_terms':[('canonical','canonical'),('redirect','リダイレクト'),('ctr','CTR')],
'related_articles':[('nofollow-dofollow-guide.html','nofollowとdofollowの違いを調べた')],
})

# --- 11. index-registration ---
TERMS.append({'slug':'index-registration','title':'インデックス登録とは？Googleにページを認識してもらう仕組み｜ツバサのメモ帳','meta_desc':'インデックス登録はGoogleがWebページをデータベースに記録し、検索結果に表示できる状態にすること。Search Consoleでのインデックスリクエスト手順と登録されない場合の対処法をまとめた。','keywords':'インデックス登録 とは,Google インデックス,Search Console インデックスリクエスト,インデックスされない 原因','og_desc':'Googleのインデックス登録の仕組みと対処法をまとめた備忘録。','breadcrumb_label':'インデックス登録','h1':'インデックス登録とは？<br>Googleにページを認識してもらう仕組み',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログの記事を公開しても、Google検索に全然出てこない時期があった。原因を調べたら「インデックスされていない」という状態だと分かった。</p>
<h2>インデックス登録とは</h2>
<p>Googleのクローラーがページを巡回し、その内容をGoogleのデータベースに記録することを「インデックス登録」と呼ぶ。インデックスに登録されたページだけが検索結果に表示される。つまり、どんなに良い記事を書いても、インデックスされなければ検索からは見つけてもらえない。</p>
<h2>インデックスされるまでの流れ</h2>
<h3>クロール → インデックス → ランキング</h3>
<p>Googleのクローラーがサイトを巡回（クロール）し、ページの内容を分析してデータベースに登録（インデックス）し、検索クエリに対して順位づけ（ランキング）する。この3段階を経て初めて検索結果に表示される。</p>
<h3>インデックスリクエストで催促できる</h3>
<p>Google Search ConsoleのURLインスペクションツールで、特定のURLのインデックス登録をリクエストできる。新規ページや更新したページのインデックスを早めたいときに使う。ただし1日あたりの送信回数には上限がある。</p>
<h2>覚えておきたいポイント</h2>
<h3>インデックス登録は保証されない</h3>
<p>クロールされてもインデックスされないことがある。ページの内容が薄い、重複コンテンツと判断された、サイト全体の品質が低いなどの理由でGoogleがインデックスを見送ることがある。</p>
<h3>新規サイトはインデックスに時間がかかる</h3>
<p>ドメインの信頼性が低い新規サイトは、サイトマップを送信してもインデックスされるまで数週間かかることがある。地道にサイトマップ送信とインデックスリクエストを続ける必要がある。</p>''',
'faqs':[('インデックス登録とは何ですか？','GoogleのクローラーがWebページを巡回し、内容をGoogleのデータベースに記録することです。インデックスされたページだけがGoogle検索結果に表示されます。'),('インデックスされたか確認する方法は？','Google Search ConsoleのURLインスペクションツールにURLを入力すると、インデックス登録状況を確認できます。または検索窓に「site:自分のURL」と入力する方法もあります。'),('インデックスリクエストとは何ですか？','Search ConsoleからGoogleに対して特定ページのインデックス登録を依頼することです。新規ページや更新ページのインデックスを早めたいときに使います。'),('インデックスされない原因は何ですか？','ページの内容が薄い、重複コンテンツがある、robots.txtでブロックされている、noindexタグが設定されているなどの原因が考えられます。'),('インデックスされるまでどのくらいかかりますか？','新規サイトでは1〜3週間かかることがあります。既存サイトへの新規ページ追加なら数日〜1週間が目安です。サイトマップの送信で多少早まることがあります。')],
'related_terms':[('sitemap','サイトマップ'),('robots-txt','robots.txt'),('canonical','canonical')],
'related_articles':[('google-index-not-found.html','Googleにインデックスされるまで')],
})

# --- 12. LLMO ---
TERMS.append({'slug':'llmo','title':'LLMO（LLM最適化）とは？AIに引用されるコンテンツ設計の話｜ツバサのメモ帳','meta_desc':'LLMO（LLM Optimization）はChatGPTやPerplexityなどのAIチャットボットに自サイトの情報を引用してもらうための最適化手法。SEOとの違いとllms.txt・構造化データの活用法をまとめた。','keywords':'LLMO とは,LLM最適化,AI 引用,llms.txt,AI SEO','og_desc':'LLMOの概念とSEOとの違いをまとめた備忘録。','breadcrumb_label':'LLMO','h1':'LLMO（LLM最適化）とは？<br>AIに引用されるコンテンツ設計の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>SEOに加えて「LLMO」という言葉を見かけるようになった。Google検索だけでなく、ChatGPTやPerplexityのようなAIチャットボットにも自分のサイトを参照してもらうための施策らしい。</p>
<h2>LLMOとは</h2>
<p>LLMOはLLM Optimization（大規模言語モデル最適化）の略で、AIチャットボットが回答を生成する際に、自サイトの情報を参照・引用してもらうことを目指す取り組みだ。SEOが「Google検索結果で上位に表示されること」を目指すのに対し、LLMOは「AIの回答に自サイトの情報が含まれること」を目指す。</p>
<h2>SEOとLLMOの違い</h2>
<h3>SEO：検索結果の順位を上げる</h3>
<p>ユーザーがGoogleで検索したとき、自分のページが上位に表示されることを目指す。キーワード最適化やリンク構築が主な手法。</p>
<h3>LLMO：AIの回答に情報を含めてもらう</h3>
<p>ユーザーがChatGPTやPerplexityに質問したとき、その回答に自サイトの情報や名前が出てくることを目指す。構造化データ、明確な文章構造、llms.txtの設置などが有効とされている。</p>
<h2>実践していること</h2>
<h3>llms.txtの設置</h3>
<p>llms.txtはAIがサイトの概要を把握するためのテキストファイルで、サイトのルートに設置する。robots.txtの「AI版」のようなものだ。</p>
<h3>FAQ構造化データの充実</h3>
<p>各記事にFAQセクションをJSON-LDで構造化データとして記述している。AIは構造化されたQ&Aを引用しやすいとされている。</p>''',
'faqs':[('LLMOとは何ですか？','LLM Optimizationの略で、ChatGPTやPerplexityなどのAIチャットボットに自サイトの情報を引用してもらうための最適化手法です。'),('LLMOとSEOの違いは？','SEOはGoogle検索結果での上位表示を目指します。LLMOはAIチャットボットの回答に自サイトの情報を含めてもらうことを目指します。両方を組み合わせるのが理想的です。'),('LLMOに効果的な施策は？','FAQ構造化データの充実、明確な文章構造、llms.txtの設置、結論を先に書く記事構成などが有効とされています。'),('llms.txtとは何ですか？','AIがサイトの概要を把握するためのテキストファイルで、サイトのルートディレクトリに設置します。サイトの構成や各ページの要約を記述します。'),('LLMOは個人ブログでも必要ですか？','AI検索の利用者が増えている状況を考えると、個人ブログでも意識しておくメリットはあります。SEOの延長線上で、大きな追加コストなく実施できる施策が多いです。')],
'related_terms':[('json-ld','JSON-LD'),('meta-description','meta description'),('sitemap','サイトマップ')],
'related_articles':[('llmo-article-writing.html','AIに引用されやすい記事の書き方'), ('llms-txt-setup.html','llms.txtを設置した記録')],
})

# --- 13〜20: git/GitHub系 + HTML/CSS ---

for t in [
{'slug':'git','title':'gitとは？ファイルの変更履歴を記録するツールの話｜ツバサのメモ帳','meta_desc':'gitはファイルの変更履歴を管理するバージョン管理ツール。プログラマー以外でもブログ運営やドキュメント管理で使われている。基本的な概念と用語をまとめた。','keywords':'git とは,バージョン管理 とは,git 初心者,git 使い方','og_desc':'gitの基本概念と用語をまとめた備忘録。','breadcrumb_label':'git','h1':'gitとは？<br>ファイルの変更履歴を記録するツールの話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>GitHub Pagesでブログを始めるとき、避けて通れなかったのがgitだ。最初は「プログラマーが使うもの」としか思っていなかったが、やっていることは意外と単純だった。</p>
<h2>gitとは</h2>
<p>gitはファイルの変更履歴を記録・管理するツールだ。いつ、誰が、どのファイルを、どう変更したかを記録してくれる。WordやExcelの「元に戻す」機能の超強力版と考えるとイメージしやすい。</p>
<p>gitを使うと、間違えた変更を元に戻す、過去の状態と比較する、複数人で同じファイルを同時に編集するといったことができる。もともとはLinux（OS）の開発のために作られたツールだが、今ではプログラマー以外にもブログ運営やドキュメント管理で使われている。</p>
<h2>非エンジニアが知っておくべき概念</h2>
<h3>リポジトリ</h3>
<p>ファイルと変更履歴をまとめて保管する場所。ブログで言えば「記事やCSSを全部入れたフォルダ」のようなもの。</p>
<h3>コミット</h3>
<p>「この変更を記録する」という操作。変更を加えたらコミットして履歴に残す。メモ（コミットメッセージ）を付けて何を変えたか書いておく。</p>
<h3>プッシュ</h3>
<p>自分のPCにある変更を、インターネット上のリポジトリ（GitHubなど）に送信する操作。プッシュするとサイトが更新される。</p>
<h2>覚えておきたいポイント</h2>
<h3>AIに操作を任せられる</h3>
<p>git操作はClaude Codeのようなツールに指示を出して実行させることもできる。コマンドを覚える必要はないが、コミットやプッシュの概念は理解しておいた方がよい。</p>''',
'faqs':[('gitとは何ですか？','ファイルの変更履歴を記録・管理するバージョン管理ツールです。いつ誰がどのファイルをどう変更したかを追跡できます。'),('gitはプログラマー以外でも使いますか？','はい。ブログ運営、ドキュメント管理、デザインファイルの管理など、プログラミング以外の用途でも使われています。'),('gitとGitHubの違いは？','gitはファイルの変更履歴を管理するツールで、GitHubはgitのリポジトリをインターネット上にホスティングするサービスです。gitが道具、GitHubが道具を置く場所と考えるとわかりやすいです。'),('gitを使うにはプログラミングが必要ですか？','プログラミングは不要ですが、ターミナル（コマンドライン）での操作が基本です。GUIアプリやAIツールを使えばコマンドを打たずに操作することも可能です。'),('gitの変更を元に戻すことはできますか？','できます。コミットの履歴が残っているため、過去の任意の状態に戻すことが可能です。これがgitの最大のメリットの一つです。')],
'related_terms':[('github','GitHub'),('github-pages','GitHub Pages'),('commit','コミット'),('push','プッシュ'),('repository','リポジトリ')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
{'slug':'github','title':'GitHubとは？gitのリポジトリを管理するWebサービスの話｜ツバサのメモ帳','meta_desc':'GitHubはgitリポジトリをインターネット上で管理・共有するWebサービス。無料でアカウント作成でき、GitHub Pagesを使えば静的サイトのホスティングも無料でできる。','keywords':'GitHub とは,GitHub 使い方,GitHub 無料,GitHub リポジトリ','og_desc':'GitHubの基本概念と無料で使える機能をまとめた備忘録。','breadcrumb_label':'GitHub','h1':'GitHubとは？<br>gitのリポジトリを管理するWebサービスの話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログを始めるまでGitHubというサービスの存在自体を知らなかった。エンジニアのためのサービスだと思っていたが、ブログのホスティングに使えると知って登録した。</p>
<h2>GitHubとは</h2>
<p>GitHubは、gitで管理するリポジトリ（ファイルの保管場所）をインターネット上に置けるWebサービスだ。Microsoft傘下の企業が運営している。無料プランでも十分な機能が使え、個人のブログ運営やドキュメント管理に利用されている。</p>
<p>gitがファイルの変更履歴を記録するツールなら、GitHubはそのツールの「置き場」にあたる。自分のPC（ローカル）で作業した結果をGitHubにアップロード（プッシュ）すると、インターネット経由でどこからでもアクセスできる。</p>
<h2>ブログ運営での使い方</h2>
<h3>GitHub Pagesで無料ホスティング</h3>
<p>GitHubにはGitHub Pagesという機能があり、リポジトリに置いたHTMLファイルをそのままWebサイトとして公開できる。レンタルサーバー不要で、費用は0円。</p>
<h3>バージョン管理で安心</h3>
<p>記事の変更履歴がすべてGitHubに残るため、間違えた編集を元に戻したり、いつ何を変更したかを後から確認できる。</p>
<h2>覚えておきたいポイント</h2>
<h3>リポジトリは公開設定に注意</h3>
<p>GitHub Pagesを使う場合、リポジトリは公開（Public）設定になる。コミット履歴にメールアドレスや本名が入らないよう、gitの設定を匿名用にしておくことをおすすめする。</p>''',
'faqs':[('GitHubとは何ですか？','gitリポジトリをインターネット上で管理・共有するWebサービスです。Microsoft傘下の企業が運営しており、無料プランでも十分に使えます。'),('GitHubは無料で使えますか？','はい。無料プランでリポジトリの作成・管理・GitHub Pagesの利用が可能です。有料プランではプライベートリポジトリの高度な機能が使えます。'),('GitHubとgitの違いは？','gitはファイルの変更履歴を管理するツールで、GitHubはgitリポジトリをインターネット上に置くサービスです。gitが道具、GitHubが保管場所です。'),('GitHubのアカウント作成に必要なものは？','メールアドレスがあればアカウントを作成できます。クレジットカードは不要です。'),('GitHubで個人情報は公開されますか？','パブリックリポジトリではコミット履歴が公開されます。gitの設定でユーザー名とメールアドレスを匿名用に変更しておくことを推奨します。')],
'related_terms':[('git','git'),('github-pages','GitHub Pages'),('repository','リポジトリ')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話'),('github-pages-vs-note.html','noteでなくGitHub Pagesを選んだ理由')],
},
{'slug':'github-pages','title':'GitHub Pagesとは？無料で使える静的サイトホスティングの話｜ツバサのメモ帳','meta_desc':'GitHub PagesはGitHubリポジトリからHTMLファイルをそのままWebサイトとして公開できる無料サービス。レンタルサーバー不要でブログ運営ができる仕組みをまとめた。','keywords':'GitHub Pages とは,GitHub Pages 無料,静的サイト ホスティング,GitHub Pages ブログ','og_desc':'GitHub Pagesの仕組みと無料でブログを運営できる理由をまとめた備忘録。','breadcrumb_label':'GitHub Pages','h1':'GitHub Pagesとは？<br>無料で使える静的サイトホスティングの話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>このブログはGitHub Pagesで運営している。レンタルサーバー代は0円。HTMLファイルをGitHubにアップロードするだけでサイトが公開される仕組みだ。</p>
<h2>GitHub Pagesとは</h2>
<p>GitHubのリポジトリに置いたHTMLファイルを、そのままWebサイトとして公開できるサービスだ。「ユーザー名.github.io」というURLが無料で使え、独自ドメインの設定もできる。</p>
<p>「静的サイト」（HTMLファイルをそのまま表示するサイト）専用のサービスで、WordPressのようなデータベースを使うサイトは公開できない。そのかわりサーバー管理が不要で、セキュリティリスクが低い。</p>
<h2>ブログ運営に使えるのか</h2>
<h3>AdSense・アフィリエイトも設置可能</h3>
<p>HTMLを自由に書けるため、Google AdSenseやAmazon アソシエイトのタグを設置できる。noteのようにプラットフォーム側の制約がない。</p>
<h3>SEO・LLMO施策を自由に実装できる</h3>
<p>meta description、構造化データ、llms.txt、サイトマップなど、HTMLに関わるSEO施策をすべて自分でコントロールできる。</p>
<h2>覚えておきたいポイント</h2>
<h3>記事の更新にはgit操作が必要</h3>
<p>ブラウザで記事を書いてボタンを押せば公開、というわけにはいかない。HTMLファイルを編集してgitでプッシュする手順が必要。AIツールを使えばこの手順は大幅に簡略化できる。</p>
<h3>帯域幅の制限がある</h3>
<p>GitHubの公式によると、GitHub Pagesの帯域は月100GBの制限がある。個人ブログ規模なら問題にならないが、大量のアクセスがあるサイトでは注意が必要。</p>''',
'faqs':[('GitHub Pagesとは何ですか？','GitHubリポジトリに置いたHTMLファイルをWebサイトとして公開できる無料のホスティングサービスです。レンタルサーバー不要でブログ運営ができます。'),('GitHub Pagesは無料ですか？','はい。GitHubアカウントがあれば無料で使えます。独自ドメインを取得する場合は年間1,500円程度の費用がかかります。'),('GitHub PagesでWordPressは使えますか？','使えません。GitHub Pagesは静的サイト専用で、PHPやデータベースを使うWordPressは動作しません。HTMLファイルをそのまま配信するサービスです。'),('GitHub Pagesの制限は何がありますか？','リポジトリ容量1GB、帯域月100GB、ビルド時間10分以内などの制限があります。個人ブログ規模であれば問題になることはほぼありません。'),('GitHub PagesでAdSenseは使えますか？','使えます。HTMLを自由に記述できるため、AdSenseの広告コードを設置可能です。審査もGitHub Pagesだからといって不利になることはありません。')],
'related_terms':[('github','GitHub'),('git','git'),('html','HTML'),('css','CSS')],
'related_articles':[('github-pages-vs-note.html','noteでなくGitHub Pagesを選んだ理由'),('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話'),('static-vs-dynamic-site.html','静的サイトと動的サイトの違い')],
},
{'slug':'commit','title':'コミット（commit）とは？gitで変更を記録する操作の話｜ツバサのメモ帳','meta_desc':'コミット（commit）はgitでファイルの変更を履歴に記録する操作。変更内容を説明するコミットメッセージの書き方と、コミットの基本的な概念をまとめた。','keywords':'コミット とは,git commit,コミットメッセージ 書き方,git 変更記録','og_desc':'gitのコミット操作の基本概念をまとめた備忘録。','breadcrumb_label':'コミット','h1':'コミット（commit）とは？<br>gitで変更を記録する操作の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログの記事を編集した後に「コミットしてください」と言われて何のことかわからなかった。コミットはgitで最も基本的な操作の一つだ。</p>
<h2>コミットとは</h2>
<p>コミットは、ファイルに加えた変更をgitの履歴に「記録する」操作だ。ゲームで言うセーブポイントのようなもので、コミットするたびにその時点のファイルの状態が保存される。</p>
<p>コミットにはメッセージ（コミットメッセージ）を付ける。「記事Aのタイトルを修正」「サイトマップにURLを追加」のように、何を変えたかを簡潔に書いておくと、あとで履歴を見返すときに便利だ。</p>
<h2>コミットの使い方</h2>
<h3>作業のまとまりごとにコミットする</h3>
<p>「記事の追加」と「サイトマップの更新」のように関連する変更はまとめてコミットし、無関係な変更は別のコミットに分けるのが基本。このブログでは記事追加時に、HTML・サムネイル・サイトマップ・llms.txtを1つのコミットにまとめている。</p>
<h2>覚えておきたいポイント</h2>
<h3>コミットしただけではサイトは更新されない</h3>
<p>コミットはあくまでローカル（自分のPC）での記録。サイトに反映するにはプッシュ（GitHubにアップロード）が別途必要だ。</p>
<h3>コミットは取り消せる</h3>
<p>間違えたコミットは取り消すことができる。ただし操作が複雑になりがちなので、コミット前にファイルの内容をよく確認するのが望ましい。</p>''',
'faqs':[('コミットとは何ですか？','gitでファイルの変更を履歴に記録する操作です。変更内容を説明するメッセージを付けて保存します。'),('コミットメッセージは何を書けばよいですか？','何を変更したかを簡潔に書きます。例：「記事Aのタイトルを修正」「サイトマップにURL追加」など。日本語でも英語でも構いません。'),('コミットしたらすぐサイトに反映されますか？','いいえ。コミットはローカルでの記録で、サイトに反映するにはプッシュ操作が別途必要です。'),('コミットを取り消すことはできますか？','できます。git revertやgit resetなどのコマンドで取り消せますが、操作がやや複雑です。AIに手順を聞きながら進めるのが安全です。'),('コミットはどのくらいの頻度でするものですか？','作業の意味的なまとまりごとにコミットするのが一般的です。記事の追加・CSSの修正など、1つの目的に対して1回のコミットが目安です。')],
'related_terms':[('git','git'),('push','プッシュ'),('repository','リポジトリ')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
{'slug':'push','title':'プッシュ（push）とは？ローカルの変更をGitHubに送る操作の話｜ツバサのメモ帳','meta_desc':'プッシュ（git push）はローカルPCのコミット履歴をGitHubなどのリモートリポジトリに送信する操作。GitHub Pagesではプッシュ後にサイトが自動で更新される。','keywords':'push とは,git push,プッシュ git,GitHub 更新','og_desc':'gitのプッシュ操作の仕組みをまとめた備忘録。','breadcrumb_label':'プッシュ','h1':'プッシュ（push）とは？<br>ローカルの変更をGitHubに送る操作の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>ブログの記事を追加してコミットしたあと、「pushしてください」と言われる。このプッシュをしないとサイトが更新されないのだが、最初はコミットとの違いがわからなかった。</p>
<h2>プッシュとは</h2>
<p>プッシュ（git push）は、自分のPC（ローカルリポジトリ）で記録したコミットを、GitHubなどのリモートリポジトリに送信する操作だ。コミットが「手元で保存」なら、プッシュは「アップロード」にあたる。</p>
<p>GitHub Pagesでブログを運営している場合、プッシュするとGitHubが自動的にサイトを再構築し、数分以内に変更がライブサイトに反映される。</p>
<h2>プッシュの流れ</h2>
<h3>ファイル編集 → コミット → プッシュ</h3>
<p>この3ステップがgitの基本的な作業フローだ。ファイルを編集し、変更をコミットで記録し、プッシュでGitHubに送信する。プッシュを忘れるとサイトが更新されない。</p>
<h2>覚えておきたいポイント</h2>
<h3>プッシュ前にコミット内容を確認する</h3>
<p>一度プッシュした変更は公開される。特にGitHub Pagesでは即座にサイトに反映されるため、間違った内容をプッシュしないよう注意する。</p>
<h3>プッシュに失敗することがある</h3>
<p>リモートリポジトリの内容がローカルと食い違っていると、プッシュが拒否されることがある（コンフリクト）。この場合はプル（リモートの内容をローカルに取り込む）してから再度プッシュする必要がある。</p>''',
'faqs':[('プッシュとは何ですか？','ローカルPCで記録したコミットをGitHubなどのリモートリポジトリに送信する操作です。プッシュするとサイトが更新されます。'),('プッシュとコミットの違いは？','コミットはローカルで変更を記録する操作、プッシュはその記録をリモートに送信する操作です。コミットだけではサイトは更新されません。'),('プッシュに失敗する原因は？','リモートリポジトリの内容がローカルと食い違っている場合に発生します。プル操作でリモートの内容を取り込んでから再度プッシュします。'),('プッシュしたあとサイトに反映されるまで何分かかりますか？','GitHub Pagesの場合、通常は1〜5分程度で反映されます。GitHubのステータスページで障害がないか確認できます。'),('プッシュを取り消すことはできますか？','可能ですが、すでに公開された内容を取り消す操作になるため慎重に行う必要があります。AIに手順を聞きながら対処するのが安全です。')],
'related_terms':[('git','git'),('commit','コミット'),('repository','リポジトリ'),('github','GitHub')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
{'slug':'repository','title':'リポジトリとは？ファイルと変更履歴を保管する場所の話｜ツバサのメモ帳','meta_desc':'リポジトリ（repository）はgitでファイルと変更履歴を保管する場所。ローカルリポジトリとリモートリポジトリの違い、GitHub上での作成方法をまとめた。','keywords':'リポジトリ とは,repository git,リモートリポジトリ,ローカルリポジトリ','og_desc':'gitのリポジトリの概念と種類をまとめた備忘録。','breadcrumb_label':'リポジトリ','h1':'リポジトリとは？<br>ファイルと変更履歴を保管する場所の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>GitHubに登録した直後に「リポジトリを作成してください」と表示されて、何を作ればいいのか戸惑った。リポジトリは「ファイルを入れておく箱」のようなものだ。</p>
<h2>リポジトリとは</h2>
<p>リポジトリ（repository、略してrepo）は、ファイルとその変更履歴をまとめて保管する場所だ。ブログで言えば「記事HTML、CSS、画像、サイトマップなどの全ファイル＋いつ何を変えたかの記録」が入った箱にあたる。</p>
<h2>ローカルとリモートの2種類</h2>
<h3>ローカルリポジトリ</h3>
<p>自分のPC上にあるリポジトリ。ファイルの編集やコミットはここで行う。</p>
<h3>リモートリポジトリ</h3>
<p>GitHub上にあるリポジトリ。ローカルの変更をプッシュして同期する。他の人やツールとファイルを共有するための場所。GitHub Pagesの場合、リモートリポジトリの内容がそのままWebサイトとして公開される。</p>
<h2>覚えておきたいポイント</h2>
<h3>リポジトリ名がURLの一部になる</h3>
<p>GitHub Pagesの場合、「ユーザー名.github.io」というリポジトリ名にすると、そのままURLになる。リポジトリ名は後から変更できるが、URLも変わるので注意。</p>''',
'faqs':[('リポジトリとは何ですか？','gitでファイルと変更履歴をまとめて保管する場所です。ブログの全ファイルとその編集記録が入った箱のようなものです。'),('ローカルリポジトリとリモートリポジトリの違いは？','ローカルは自分のPC上、リモートはGitHubなどインターネット上にあるリポジトリです。ローカルで編集してプッシュでリモートに同期します。'),('リポジトリの作り方は？','GitHubのWebサイトで「New repository」ボタンから作成できます。リポジトリ名、公開設定などを選ぶだけです。'),('リポジトリは無料で作れますか？','はい。GitHubの無料プランで公開リポジトリを無制限に作成できます。'),('リポジトリのサイズに制限はありますか？','GitHubでは1リポジトリあたり推奨5GB以内、1ファイル100MB以内の制限があります。テキストベースのブログなら問題になることはほぼありません。')],
'related_terms':[('git','git'),('github','GitHub'),('commit','コミット'),('push','プッシュ')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
{'slug':'html','title':'HTMLとは？Webページの構造を作るマークアップ言語の話｜ツバサのメモ帳','meta_desc':'HTMLはWebページの構造を定義するマークアップ言語。見出し・段落・リンク・画像などのタグでページの骨組みを作る。ブログ運営で最低限知っておくべき基本をまとめた。','keywords':'HTML とは,HTML 基本,マークアップ言語,HTML タグ','og_desc': 'HTMLの基本概念とブログ運営での使い方をまとめた備忘録。','breadcrumb_label':'HTML','h1':'HTMLとは？<br>Webページの構造を作るマークアップ言語の話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>GitHub Pagesでブログを作るにはHTMLファイルが必要だ。プログラミング言語のように聞こえるが、実際は「ここが見出し」「ここが段落」とWebブラウザに教えるための印付けにすぎない。</p>
<h2>HTMLとは</h2>
<p>HTML（HyperText Markup Language）は、Webページの構造を定義するマークアップ言語だ。&lt;h1&gt;で見出し、&lt;p&gt;で段落、&lt;a&gt;でリンク、&lt;img&gt;で画像というように、タグと呼ばれる印で内容を囲んで構造を伝える。</p>
<p>HTMLはプログラミング言語ではない。条件分岐やループといった処理は書けず、あくまでも「ページの構造」を定義するものだ。見た目のデザインはCSSが担当する。</p>
<h2>ブログ運営で最低限知っておくこと</h2>
<h3>よく使うタグ</h3>
<p>&lt;title&gt;（ページタイトル）、&lt;meta&gt;（ページの説明文）、&lt;h2&gt;（見出し）、&lt;p&gt;（段落）、&lt;a&gt;（リンク）、&lt;img&gt;（画像）あたりが頻出する。テンプレートを一度作ってしまえば、中身を入れ替えるだけで記事が作れる。</p>
<h2>覚えておきたいポイント</h2>
<h3>AIにHTMLを書いてもらうことができる</h3>
<p>HTMLの構文を完璧に覚える必要はない。AIに「こういう構成のページを作って」と伝えれば、HTMLファイルを生成してくれる。自分はHTMLの仕組みを大まかに理解し、出力を確認・修正指示する役割に集中できる。</p>''',
'faqs':[('HTMLとは何ですか？','Webページの構造を定義するマークアップ言語です。タグで見出し・段落・リンクなどを指定し、ブラウザが表示できる形にします。プログラミング言語ではありません。'),('HTMLを覚えないとブログは作れませんか？','AIに書いてもらうことができるため、完璧に覚える必要はありません。ただし基本的なタグの意味を理解しておくと、AIの出力を確認・修正しやすくなります。'),('HTMLとCSSの違いは？','HTMLはページの構造（見出し・段落・リンクなど）を定義し、CSSはページの見た目（色・フォント・レイアウトなど）を定義します。'),('HTMLファイルの拡張子は？','.htmlです。テキストエディタで編集でき、Webブラウザで直接開いて表示を確認できます。'),('HTMLのバージョンは何がありますか？','現在の主流はHTML5です。以前のバージョン（HTML4、XHTML）と比べて、動画や音声の埋め込み、セマンティックなタグが充実しています。')],
'related_terms':[('css','CSS'),('json-ld','JSON-LD'),('meta-description','meta description'),('alt-attribute','alt属性')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
{'slug':'css','title':'CSSとは？Webページの見た目を整えるスタイルシートの話｜ツバサのメモ帳','meta_desc':'CSS（Cascading Style Sheets）はWebページの色・フォント・レイアウトなど見た目を定義するスタイルシート言語。HTMLと組み合わせてデザインを作る仕組みをまとめた。','keywords':'CSS とは,スタイルシート 基本,CSS HTML 違い,CSS デザイン','og_desc':'CSSの基本概念とHTMLとの役割分担をまとめた備忘録。','breadcrumb_label':'CSS','h1':'CSSとは？<br>Webページの見た目を整えるスタイルシートの話',
'body':'''<p>こんにちは、ツバサです。</p>
<p>HTMLでブログの骨組みができたあと、「デザインはCSSで調整します」と言われた。CSSはHTMLが作った構造に「色」や「形」を付ける役割を担っている。</p>
<h2>CSSとは</h2>
<p>CSS（Cascading Style Sheets）は、Webページの見た目を定義するスタイルシート言語だ。文字の色、フォント、余白、背景色、レイアウトなど、ページのデザインに関わる部分を指定する。</p>
<p>HTMLが「ここは見出し、ここは段落」と構造を定義し、CSSが「見出しは青色で太字、段落は16pxでグレー」と見た目を定義する。この2つを組み合わせてWebページが完成する。</p>
<h2>ブログ運営での使い方</h2>
<h3>テンプレートのstyleタグで一括管理</h3>
<p>このブログではHTMLファイル内の&lt;style&gt;タグにCSSを書いている。一度デザインを決めてしまえば、全ページで同じ見た目を維持できる。</p>
<h3>レスポンシブデザイン</h3>
<p>CSSの@mediaクエリを使うと、PC・スマホ・タブレットそれぞれに最適なレイアウトを指定できる。このブログも画面幅600px以下でフォントサイズやレイアウトを切り替えている。</p>
<h2>覚えておきたいポイント</h2>
<h3>CSSもAIに書いてもらえる</h3>
<p>「落ち着いた配色にしてほしい」「スマホでも読みやすいデザインにして」のような指示でAIがCSSを生成してくれる。CSSの文法を覚えるより、デザインの要望を言語化する方が重要だ。</p>''',
'faqs':[('CSSとは何ですか？','Webページの色・フォント・レイアウトなどの見た目を定義するスタイルシート言語です。HTMLが構造を作り、CSSがデザインを付けます。'),('CSSとHTMLの違いは？','HTMLはページの構造（見出し・段落など）を定義し、CSSは見た目（色・フォント・余白など）を定義します。両方を組み合わせてWebページが完成します。'),('CSSを知らなくてもブログは作れますか？','AIに要望を伝えてCSSを生成してもらうことができるため、文法を完璧に覚える必要はありません。'),('レスポンシブデザインとは何ですか？','PC・スマホ・タブレットなど画面サイズに応じてレイアウトを切り替えるデザイン手法です。CSSの@mediaクエリで実装します。'),('CSSはどこに書きますか？','HTMLファイル内のstyleタグに書く方法と、別ファイル（.css）に書いてHTMLから読み込む方法があります。このブログではstyleタグ内に記述しています。')],
'related_terms':[('html','HTML'),('responsive','レスポンシブ'),('first-view','ファーストビュー')],
'related_articles':[('ai-blog-building.html','AIに聞きながらGitHub Pagesでブログを構築した話')],
},
]:
    TERMS.append(t)

# ============================================================
# HTML生成
# ============================================================

os.makedirs('glossary', exist_ok=True)
generated = []

for term in TERMS:
    jsonld = make_jsonld(term.get('faqs', []))
    related_terms_html = make_related_terms(term.get('related_terms', []))
    related_articles_html = make_related_articles(term.get('related_articles', []))

    html = TEMPLATE.format(
        title=term['title'],
        meta_desc=term['meta_desc'],
        keywords=term['keywords'],
        og_desc=term['og_desc'],
        slug=term['slug'],
        jsonld=jsonld,
        breadcrumb_label=term['breadcrumb_label'],
        h1=term['h1'],
        body=term['body'],
        related_terms_html=related_terms_html,
        related_articles_html=related_articles_html,
    )

    path = f"glossary/{term['slug']}.html"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    generated.append(term)
    print(f"✅ {path}")

print(f"\n=== {len(generated)}ファイル生成完了 ===")

# ============================================================
# sitemap.xml 更新
# ============================================================

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

added_sitemap = 0
for term in generated:
    url = f"https://tsubasa-memo.github.io/glossary/{term['slug']}.html"
    if url not in sitemap:
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>"""
        sitemap = sitemap.replace('</urlset>', entry)
        added_sitemap += 1

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print(f"✅ sitemap.xml: {added_sitemap}件追加")

# ============================================================
# llms.txt 更新
# ============================================================

with open('llms.txt', 'r', encoding='utf-8') as f:
    llms = f.read()

added_llms = 0
for term in generated:
    url = f"https://tsubasa-memo.github.io/glossary/{term['slug']}.html"
    if url not in llms:
        # llms.txt doesn't list individual glossary pages, skip
        added_llms += 1

# Glossary pages are linked from the glossary index, not individually in llms.txt
print(f"ℹ️  llms.txt: 用語集は索引ページからリンクされるため個別追加なし")

print(f"\n=== 全処理完了 ===")
print(f"生成ファイル: {len(generated)}件")
print(f"サイトマップ追加: {added_sitemap}件")

# ============================================================
# glossary/index.html 更新
# ============================================================

INDEX_CARDS = [
    ('ctr', 'analytics', 'CTR', 'EC分析', '表示回数に対するクリック数の割合。'),
    ('meta-description', 'web', 'meta description', 'Web・SEO', '検索結果に表示されるページ説明文のHTMLタグ。'),
    ('canonical', 'web', 'canonical', 'Web・SEO', 'URLの正規化。重複ページの評価を1つに集約する。'),
    ('json-ld', 'web', 'JSON-LD', 'Web・SEO', '検索結果にFAQなどを表示させる構造化データ形式。'),
    ('sitemap', 'web', 'サイトマップ', 'Web・SEO', 'サイト内の全ページ一覧をXMLで記述したファイル。'),
    ('robots-txt', 'web', 'robots.txt', 'Web・SEO', 'クローラーに巡回範囲を指示するテキストファイル。'),
    ('redirect', 'web', 'リダイレクト', 'Web・SEO', 'URLを別のURLに自動転送する仕組み。'),
    ('exif', 'image', 'Exif', '画像・ファイル', '写真に自動記録される撮影日時・位置情報などのメタデータ。'),
    ('breadcrumb', 'web', 'パンくずリスト', 'Web・SEO', 'サイト内の階層構造を示すナビゲーション。'),
    ('nofollow', 'web', 'nofollow', 'Web・SEO', 'リンク先にページ評価を渡さないrel属性。'),
    ('index-registration', 'web', 'インデックス登録', 'Web・SEO', 'Googleがページをデータベースに記録すること。'),
    ('llmo', 'web', 'LLMO', 'Web・SEO', 'AIチャットボットに情報を引用してもらうための最適化。'),
    ('git', 'web', 'git', 'Web・開発', 'ファイルの変更履歴を記録するバージョン管理ツール。'),
    ('github', 'web', 'GitHub', 'Web・開発', 'gitリポジトリを管理するWebサービス。'),
    ('github-pages', 'web', 'GitHub Pages', 'Web・開発', 'GitHubリポジトリからサイトを無料公開できるサービス。'),
    ('commit', 'web', 'コミット', 'Web・開発', 'gitで変更を履歴に記録する操作。'),
    ('push', 'web', 'プッシュ', 'Web・開発', 'ローカルの変更をリモートリポジトリに送信する操作。'),
    ('repository', 'web', 'リポジトリ', 'Web・開発', 'ファイルと変更履歴を保管する場所。'),
    ('html', 'web', 'HTML', 'Web・開発', 'Webページの構造を定義するマークアップ言語。'),
    ('css', 'web', 'CSS', 'Web・開発', 'Webページの見た目を定義するスタイルシート。'),
]

try:
    with open('glossary/index.html', 'r', encoding='utf-8') as f:
        idx = f.read()

    added_idx = 0
    for slug, cat, name, cat_label, desc in INDEX_CARDS:
        if f'/glossary/{slug}.html' not in idx:
            card = f'<div class="term-card" data-cat="{cat}"><div class="term-header"><a href="/glossary/{slug}.html" class="term-name">{name}</a><span class="term-cat">{cat_label}</span></div><p class="term-desc">{desc}</p><a href="/glossary/{slug}.html" class="term-link">\u2192 \u3082\u3063\u3068\u8a73\u3057\u304f</a></div>\n'
            idx = idx.replace('</div>\n</main>', card + '</div>\n</main>', 1)
            added_idx += 1

    count_m = re.search(r'id="term-count">(\d+)', idx)
    if count_m:
        old = int(count_m.group(1))
        idx = idx.replace(f'id="term-count">{old}', f'id="term-count">{old + added_idx}')

    with open('glossary/index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print(f'\u2705 glossary/index.html: {added_idx}\u4ef6\u8ffd\u52a0')
except FileNotFoundError:
    print('\u26a0\ufe0f  glossary/index.html not found (run in repo directory)')

print("\n\u26a0\ufe0f  \u3042\u3068\u3084\u308b\u3053\u3068:")
print("  1. python3 build_search_index.py \u3092\u5b9f\u884c")
print("  2. git add / git commit")
