import os, textwrap

OUT = "/home/claude/blog-seo-articles/out"
os.makedirs(OUT, exist_ok=True)

GA = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YYBFXHXMM6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-YYBFXHXMM6');
</script>"""

ADSENSE = """<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6503265021738697"
     crossorigin="anonymous"></script>"""

ICONS = """<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">"""

AUTHOR = """<div class="author-box">
<div class="author-icon"><img src="icons/tsubasa.png" alt="ツバサ" width="64" height="64"></div>
<div class="author-text">
<p class="author-name">ツバサ</p>
<p>EC関係の仕事をしています。このサイトは自分が調べたことの備忘録です。Photoshopは少し使えますが苦手で、ちょっとした画像補正はもっぱらスマホアプリ派。アプリで対応しきれない本格的なレタッチはプロに依頼しています。</p>
</div>
</div>"""

CSS = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#f8f7f4;--text:#2d2d2d;--text-sub:#666;--accent:#7c3aed;--accent-light:#f3effe;--border:#e0ddd8;--card:#fff;--link:#7c3aed;--tag-bg:#f2f0ec}
body{font-family:"Noto Sans JP","Hiragino Kaku Gothic ProN",sans-serif;background:var(--bg);color:var(--text);line-height:1.85;font-size:16px;-webkit-font-smoothing:antialiased}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:780px;margin:0 auto;padding:0 20px}
header{background:#fff;border-bottom:1px solid var(--border);padding:18px 0}
header .wrap{display:flex;align-items:center;justify-content:space-between}
.site-name{font-size:14px;font-weight:700;color:var(--accent);letter-spacing:.5px}
.site-tag{font-size:11px;color:var(--text-sub);background:var(--tag-bg);padding:3px 10px;border-radius:20px}
nav.breadcrumb{font-size:13px;color:var(--text-sub);padding:12px 0;border-bottom:1px solid var(--border);background:#fff}
nav.breadcrumb a{color:var(--text-sub)}
.hero{background:linear-gradient(135deg,#7c3aed 0%,#4c1d95 100%);color:#fff;padding:56px 0 48px;text-align:center}
.hero h1{font-size:24px;line-height:1.5;font-weight:700;margin-bottom:16px;letter-spacing:.5px}
@media(min-width:640px){.hero h1{font-size:28px}}
.hero .lead{font-size:15px;opacity:.9;line-height:1.7;max-width:600px;margin:0 auto}
.updated{text-align:center;padding:12px;font-size:12px;color:var(--text-sub);background:#fff;border-bottom:1px solid var(--border)}
article{padding:40px 0 60px}
h2{font-size:22px;font-weight:700;margin:52px 0 20px;padding-bottom:10px;border-bottom:3px solid var(--accent);color:var(--text);line-height:1.4}
h2:first-of-type{margin-top:0}
h3{font-size:18px;font-weight:700;margin:36px 0 14px;color:var(--accent)}
p{margin-bottom:18px}
.point-box{background:var(--accent-light);border:1px solid var(--accent);border-radius:10px;padding:20px 24px;margin:24px 0}
.point-box ul{padding-left:20px}
.point-box li{margin-bottom:6px;font-size:15px}
.warn-box{background:#fff8e1;border:1px solid #f9a825;border-radius:10px;padding:20px 24px;margin:24px 0}
.spec-table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15px}
.spec-table th,.spec-table td{border:1px solid var(--border);padding:12px 16px;text-align:left}
.spec-table th{background:var(--tag-bg);font-weight:700;font-size:14px}
.spec-table td{background:var(--card)}
.faq-item{border:1px solid var(--border);border-radius:10px;padding:20px 24px;margin:16px 0;background:var(--card)}
.faq-item .faq-q{font-weight:700;color:var(--accent);margin-bottom:10px;font-size:16px}
.faq-item .faq-a{font-size:15px;line-height:1.75;margin:0}
.related{margin:48px 0 0}
.related h2{font-size:16px;border-bottom:2px solid var(--border);color:var(--text-sub)}
.related-list{display:flex;flex-direction:column;gap:12px;margin-top:16px}
.related-item{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:14px 18px}
.related-item a{color:var(--text);font-size:14px;font-weight:700}
.author-box{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:24px 28px;margin:48px 0 0;display:flex;gap:20px;align-items:flex-start}
.author-box .author-icon{width:64px;height:64px;flex-shrink:0;border-radius:50%;overflow:hidden}
.author-box .author-icon img{width:100%;height:100%}
.author-box .author-text p{font-size:14px;color:var(--text-sub);margin-bottom:8px;line-height:1.7}
.author-box .author-text p:last-child{margin-bottom:0}
.author-box .author-name{font-weight:700;font-size:15px;color:var(--text);margin-bottom:4px}
footer{background:#fff;border-top:1px solid var(--border);padding:32px 0;text-align:center;font-size:13px;color:var(--text-sub)}
@media(max-width:600px){.hero h1{font-size:20px}.spec-table{font-size:13px}.author-box{flex-direction:column;align-items:center;text-align:center}}
</style>"""

def build(slug, title, desc, keywords, og_desc, month, faq_ld, body, related):
    faq_json = ',\n    '.join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq_ld
    ])
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
{GA}
<meta charset="UTF-8">
{ICONS}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{ADSENSE}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:type" content="article">
<meta property="og:locale" content="ja_JP">
<meta property="og:image" content="https://tsubasa-memo.github.io/og/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://tsubasa-memo.github.io/og/{slug}.png">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://tsubasa-memo.github.io/{slug}.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_json}
  ]
}}
</script>
{CSS}
</head>
<body>
<header>
<div class="wrap">
<a href="index.html" class="site-name">ツバサのメモ帳</a>
<span class="site-tag">備忘録ブログ</span>
</div>
</header>
<nav class="breadcrumb"><div class="wrap"><a href="index.html">ホーム</a> ＞ <a href="archive.html?cat=career">副業・キャリア</a> ＞ {title[:20]}…</div></nav>
<div class="hero">
<div class="wrap">
<h1>{title}</h1>
<p class="lead">{og_desc}</p>
</div>
</div>
<div class="updated">2026年{month}月 更新</div>
<main>
<article>
<div class="wrap">
{body}
{AUTHOR}
{related}
</div>
</article>
</main>
<footer><div class="wrap">&copy; 2026 ツバサのメモ帳</div></footer>
</body>
</html>"""


# ============================================================
# 記事1: github-pages-vs-note.html
# ============================================================
articles = {}

articles['github-pages-vs-note'] = build(
    slug='github-pages-vs-note',
    title='なぜnoteじゃなくてGitHub Pagesにしたか｜AdSenseを使いたかった',
    desc='個人ブログをnoteではなくGitHub Pagesで作った理由をまとめました。AdSense非対応・Amazon Associates制限・カスタマイズの自由度など、プラットフォーム選びで調べたことの備忘録です。',
    keywords='GitHub Pages ブログ,note AdSense,個人ブログ 収益化,GitHub Pages 始め方',
    og_desc='noteではなくGitHub Pagesを選んだ理由。AdSense・Amazon Associates対応とカスタマイズ自由度で比較しました。',
    month='3',
    faq_ld=[
        ('noteとGitHub Pagesの一番の違いは何ですか？', 'noteはAdSense（Google広告）が使えないことが最大の違いです。noteはプラットフォームが広告収益を管理しており、クリエイターが自分でAdSenseコードを埋め込むことができません。GitHub Pagesは静的HTMLファイルをホスティングするサービスなので、AdSenseのスクリプトを自由に埋め込めます。'),
        ('GitHub Pagesは無料で使えますか？', '無料で使えます。GitHubアカウントを作成してリポジトリを公開設定にし、GitHub Pagesを有効にするだけで「ユーザー名.github.io」というURLでサイトが公開されます。独自ドメインの取得は有料（年間1,500円程度）ですが、github.ioドメインのままでも問題ありません。'),
        ('noteでAmazon アソシエイトは使えますか？', 'noteでもAmazon アソシエイトのリンクは貼れますが、テキストリンクや画像リンクのみです。GitHub Pagesなら商品カードのようなカスタムHTMLも自由に設置できるため、より柔軟なアフィリエイト設置が可能です。'),
        ('GitHub Pagesでブログを作るのに技術的な知識は必要ですか？', '基本的なHTMLとCSSがわかれば作れます。僕自身も最初はHTMLをほとんど書いたことがなく、AIに手伝ってもらいながら記事を書いています。テンプレートをコピーして内容を書き換えていくスタイルなので、慣れれば難しくありません。'),
        ('noteからGitHub Pagesに移行するのは難しいですか？', 'noteの記事をHTMLに変換してGitHub Pagesに移す作業は、記事数が多いと手間がかかります。最初からGitHub Pagesで始める方が楽です。僕の場合はもともとnoteに記事がなかったので、最初からGitHub Pagesで始めました。'),
        ('SEOはnoteとGitHub Pages、どちらが強いですか？', 'noteはドメイン権威（DA）が高いため短期的には検索上位に出やすい傾向があります。一方GitHub Pagesは自分でsitemap.xmlや構造化データを設置することで長期的なSEO対策ができます。収益化とSEOの両立を考えると、GitHub Pagesの方が制御しやすいと感じています。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>noteとGitHub Pages、AdSense対応の違い</li>
<li>Amazon アソシエイトの設置自由度の比較</li>
<li>GitHub Pagesを選んだ具体的な理由3つ</li>
<li>GitHub Pagesのデメリットと対策</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログを始めるとき、最初に迷ったのが「noteで書くか、自分でサイトを作るか」でした。結論を先に言うと、<strong>AdSenseを使いたかったからGitHub Pagesにした</strong>、というのが一番の理由です。</p>

<h2>noteで書かなかった理由</h2>

<p>noteはシンプルで書きやすいですし、SEOも最初は効きやすいと聞いていました。記事を書くこと自体に集中できる環境は魅力でした。ただ調べてみると、いくつか気になる制限があることがわかりました。</p>

<p>一番大きかったのは<strong>Google AdSenseが使えない</strong>という点です。noteはプラットフォーム側が広告枠を管理しており、自分のAdSenseアカウントのコードを埋め込むことができません。note独自の収益機能（有料記事・メンバーシップ）はありますが、広告収入の仕組みは別物です。</p>

<p>次に気になったのはカスタマイズの制限です。HTMLやCSSを自由に書けないため、商品比較表を作ったり、構造化データを設置したり、ページのレイアウトを変えたりといった作業ができません。SEO対策やLLMO（AIへの最適化）をやりたいなら、自分でHTMLを管理できる環境の方が都合が良いと判断しました。</p>

<h2>GitHub Pagesを選んだ理由3つ</h2>

<h3>1. AdSenseが自由に設置できる</h3>
<p>GitHub Pagesは静的なHTMLファイルをそのままホスティングするサービスなので、AdSenseのスクリプトタグをHTMLに書くだけで広告が表示されます。AdSenseの審査基準はサイトの内容によるもので、GitHub PagesかどうかはGoogle側は特に気にしません。</p>

<h3>2. 完全無料で使える</h3>
<p>GitHubのアカウントさえあれば、サイトのホスティング費用はかかりません。「ユーザー名.github.io」というURLで公開されます。独自ドメインを取得すれば年間1,500円程度の費用がかかりますが、なくても問題なく運営できます。</p>

<h3>3. HTMLを自由に書ける</h3>
<p>SEO用のmeta descriptionを丁寧に書く、FAQ構造化データ（JSON-LD）を入れる、内部リンクをコントロールする、llms.txtを設置してAIに読ませるといった対策がすべて自分の手でできます。ブログを書くだけでなく「育てる」作業をやりたい場合、プラットフォームに縛られない環境の方が動きやすいです。</p>

<h2>GitHub Pagesのデメリットと感じたこと</h2>

<p>デメリットもあります。記事を更新するにはHTMLファイルを編集してGitHubにアップロードする手順が必要なので、noteのようにブラウザ上で書いてすぐ投稿、とはいきません。最初は手順を覚えるまで時間がかかりました。</p>

<p>また、noteはドメイン権威が高いため検索上位に出やすいという特性があります。GitHub Pagesの新規サイトは最初のうちはGoogleに認識されるまで時間がかかります。実際、このブログも記事を公開してからインデックスされるまで2週間ほどかかりました（その話は<a href="google-index-not-found.html">別の記事</a>にまとめています）。</p>

<div class="warn-box">
<p><strong>注意：</strong>GitHub Pagesで運営する場合、コミット履歴に本名やメールアドレスが残ることがあります。匿名で運営したい場合はGitの設定（user.nameとuser.email）を匿名用にしておくことをおすすめします。</p>
</div>

<h2>まとめ：noteかGitHub Pagesか</h2>

<table class="spec-table">
<tr><th></th><th>note</th><th>GitHub Pages</th></tr>
<tr><td>AdSense</td><td>×（使えない）</td><td>○（自由に設置可）</td></tr>
<tr><td>Amazon アソシエイト</td><td>△（テキストリンクのみ）</td><td>○（HTMLカード等も可）</td></tr>
<tr><td>書きやすさ</td><td>◎（ブラウザで完結）</td><td>△（HTML編集が必要）</td></tr>
<tr><td>カスタマイズ</td><td>×（制限あり）</td><td>◎（自由）</td></tr>
<tr><td>初期SEO</td><td>◎（ドメイン権威が高い）</td><td>△（時間がかかる）</td></tr>
<tr><td>費用</td><td>無料（有料プランもあり）</td><td>無料</td></tr>
</table>

<p>「とにかく書くことに集中したい」ならnote、「広告・アフィリエイトで収益化したい」「SEO対策を自分でコントロールしたい」ならGitHub Pages、という選び方が実態に近いと思います。僕はブログそのものを育てる作業も面白いと思っているので、GitHub Pagesを選んでよかったと感じています。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. noteとGitHub Pagesの一番の違いは何ですか？</p><p class="faq-a">noteはAdSense（Google広告）が使えないことが最大の違いです。noteはプラットフォームが広告収益を管理しており、クリエイターが自分でAdSenseコードを埋め込むことができません。GitHub Pagesは静的HTMLをホスティングするサービスなので、AdSenseのスクリプトを自由に埋め込めます。</p></div>
<div class="faq-item"><p class="faq-q">Q. GitHub Pagesは無料で使えますか？</p><p class="faq-a">無料で使えます。GitHubアカウントを作成してリポジトリを公開設定にし、GitHub Pagesを有効にするだけで「ユーザー名.github.io」というURLでサイトが公開されます。独自ドメインの取得は有料（年間1,500円程度）ですが、github.ioドメインのままでも問題ありません。</p></div>
<div class="faq-item"><p class="faq-q">Q. noteでAmazon アソシエイトは使えますか？</p><p class="faq-a">noteでもAmazon アソシエイトのリンクは貼れますが、テキストリンクや画像リンクのみです。GitHub Pagesならカスタムの商品カードHTMLも自由に設置できます。</p></div>
<div class="faq-item"><p class="faq-q">Q. GitHub Pagesでブログを作るのに技術的な知識は必要ですか？</p><p class="faq-a">基本的なHTMLとCSSがわかれば作れます。AIに手伝ってもらいながら記事を書くことも可能で、テンプレートをコピーして内容を書き換えていくスタイルなら技術的なハードルは低いです。</p></div>
<div class="faq-item"><p class="faq-q">Q. SEOはnoteとGitHub Pages、どちらが強いですか？</p><p class="faq-a">noteはドメイン権威が高いため短期的には検索上位に出やすい傾向があります。GitHub Pagesは自分でsitemap.xmlや構造化データを設置することで長期的なSEO対策ができます。収益化とSEOの両立を考えると、GitHub Pagesの方が制御しやすいと感じています。</p></div>
<div class="faq-item"><p class="faq-q">Q. GitHub PagesでAdSense審査は通りますか？</p><p class="faq-a">通ります。GitHub Pagesかどうかはほとんど関係なく、コンテンツの質と量が審査基準になります。記事数が10本以上あり、オリジナルな内容であることが重要です。プライバシーポリシーの設置も審査通過に有効です。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="adsense-application.html">個人ブログにGoogle AdSenseを申請してみた｜審査から承認までの記録</a></div>
<div class="related-item"><a href="google-index-not-found.html">Googleにインデックスされるまで｜サイトマップ送信からの記録</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)

print("記事1: github-pages-vs-note.html 生成完了")


# ============================================================
# 記事2: adsense-application.html
# ============================================================
articles['adsense-application'] = build(
    slug='adsense-application',
    title='個人ブログにGoogle AdSenseを申請してみた｜審査から承認までの記録',
    desc='個人ブログでGoogle AdSenseに申請した記録です。申請前の準備、審査中に確認したこと、承認後の広告設置まで手順をまとめました。記事数や審査期間の目安も書いています。',
    keywords='Google AdSense 申請,AdSense 審査,個人ブログ 広告,AdSense 通過 条件',
    og_desc='個人ブログでAdSenseを申請した記録。審査前の準備・審査期間・承認後の設置まで手順をまとめました。',
    month='3',
    faq_ld=[
        ('AdSenseの審査に通るために必要な記事数は？', 'Googleは明確な基準を公開していませんが、10〜20本以上のオリジナル記事があると審査が通りやすいと言われています。記事数よりも内容の充実度（各記事1,500文字以上、コピーコンテンツなし）の方が重要です。'),
        ('AdSense審査の期間はどれくらいかかりますか？', '申請から数日〜2週間程度が一般的です。サイトのコンテンツ量や品質によって変わります。審査中はサイトのコンテンツを変更せず、通常通り更新を続けることがすすめられています。'),
        ('AdSense審査に必要なページはありますか？', 'プライバシーポリシーの設置が強く推奨されています。問い合わせページや運営者情報も用意しておくと審査通過率が上がると言われています。'),
        ('AdSenseが不承認になった場合はどうすればいいですか？', '不承認メールに理由が記載されています。「コンテンツの価値が不十分」の場合は記事の充実が必要、「ポリシー違反」の場合は該当コンテンツの修正が必要です。修正後に再申請できます。'),
        ('個人ブログのAdSense収益はどれくらいになりますか？', '月間PVが1,000〜10,000程度の個人ブログでは月数百〜数千円程度が目安です。ジャンルやクリック率によって大きく変わります。最初は収益よりサイトの育成に集中することをおすすめします。'),
        ('AdSenseとAmazon アソシエイトは同時に使えますか？', '使えます。AdSenseの広告とAmazon アソシエイトのリンクを同じページに設置することはGoogleポリシー上問題ありません。記事内容に合わせて使い分けると収益効率が上がります。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>AdSense申請前に準備したこと（記事数・プライバシーポリシー等）</li>
<li>申請から審査通過までの流れ</li>
<li>審査中にやったこと・やらなかったこと</li>
<li>承認後の広告コードの設置方法</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログにGoogle AdSenseを設置するまでの記録をまとめておきます。申請前に色々調べてわかりにくかった部分を中心に書きました。</p>

<h2>申請前に準備したこと</h2>

<p>申請前に確認したのは3点です。</p>

<h3>1. 記事数と内容の確認</h3>
<p>Googleは審査通過に必要な記事数を公開していませんが、調べた限りでは「10本以上のオリジナル記事」が最低ラインとして言われていることが多いです。記事数よりもコンテンツの質の方が重要で、コピーコンテンツや内容が薄い記事は審査に不利に働くとされています。</p>
<p>申請前に各記事が1,500文字以上あること、他サイトのコピーでないことを確認しました。</p>

<h3>2. プライバシーポリシーの設置</h3>
<p>AdSenseはユーザーのブラウザにCookieを設定するため、プライバシーポリシーの設置がAdSenseのプログラムポリシーで求められています。「このサイトはGoogle AdSenseを使用しており、Cookieを使用してユーザーへの広告配信を行います」という内容を含んだページを作成しました。</p>

<h3>3. サイトが正常に動作しているか確認</h3>
<p>404エラーのページがないか、サイトマップが正常に機能しているか、Google Search Consoleでエラーが出ていないかを確認しました。</p>

<h2>申請の手順</h2>

<p>AdSenseの申請手順は次の通りです。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li><a href="https://adsense.google.com/" target="_blank" rel="noopener noreferrer">Google AdSense</a>にアクセスしてアカウントを作成</li>
<li>サイトのURLを入力</li>
<li>AdSenseのコード（スクリプトタグ）を発行してもらい、サイトの全ページの &lt;head&gt; 内に貼る</li>
<li>「サイトをAdSenseにリンク」を実行して申請完了</li>
</ol>

<p>コードを貼ってから「サイトをAdSenseにリンク」ボタンを押すと審査が始まります。コードを貼らないと先に進めないので、この段階でHTMLファイルにスクリプトを追加してGitHubにアップロードしました。</p>

<h2>審査中にやったこと・やらなかったこと</h2>

<p>審査中は<strong>サイトの構造を大きく変えない</strong>ことを意識しました。URLを変更したりページを大量に削除したりすると、審査中のクローラーが混乱する可能性があると読んだためです。</p>
<p>一方で記事の追加は続けました。審査中だからといって更新を止める必要はなく、むしろコンテンツが増えている方が良い影響があると考えました。</p>

<div class="warn-box">
<p><strong>注意：</strong>審査中にAdSenseのコードをHTMLから削除すると審査が中断される場合があります。承認通知が来るまでコードはそのままにしておく方が安全です。</p>
</div>

<h2>承認後にやったこと</h2>

<p>承認メールが届いたら、AdSenseの管理画面で広告ユニットを作成し、表示したい場所にコードを貼ります。「自動広告」を有効にすると、Googleがページを解析して最適な場所に広告を配置してくれるため、最初はこれを使いました。</p>

<p>広告が実際に表示され始めるまで数時間〜1日程度かかることがあります。最初は自分でページを開いて広告が出ているか確認してみてください。</p>

<h2>AdSenseとAmazon アソシエイトの両立</h2>

<p>AdSense承認後にAmazon アソシエイトも申請しました。同じページにAdSenseの広告とAmazon アソシエイトのリンクを設置することはGoogleのポリシー上問題ありません。記事の内容によって使い分けると収益効率が上がります。Amazon アソシエイトの登録については<a href="amazon-associates.html">別の記事</a>にまとめています。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. AdSenseの審査に通るために必要な記事数は？</p><p class="faq-a">Googleは明確な基準を公開していませんが、10〜20本以上のオリジナル記事があると審査が通りやすいと言われています。記事数よりも内容の充実度（各記事1,500文字以上、コピーコンテンツなし）の方が重要です。</p></div>
<div class="faq-item"><p class="faq-q">Q. AdSense審査の期間はどれくらいかかりますか？</p><p class="faq-a">申請から数日〜2週間程度が一般的です。サイトのコンテンツ量や品質によって変わります。審査中はサイトのコンテンツを大きく変更せず、通常通り更新を続けることが推奨されています。</p></div>
<div class="faq-item"><p class="faq-q">Q. AdSense審査に必要なページはありますか？</p><p class="faq-a">プライバシーポリシーの設置が強く推奨されています。「このサイトはGoogle AdSenseを使用しており、Cookieを使用して広告配信を行います」という内容を含むページが必要です。</p></div>
<div class="faq-item"><p class="faq-q">Q. AdSenseが不承認になった場合はどうすればいいですか？</p><p class="faq-a">不承認メールに理由が記載されています。「コンテンツの価値が不十分」の場合は記事の充実が必要、「ポリシー違反」の場合は該当コンテンツの修正が必要です。修正後に再申請できます。</p></div>
<div class="faq-item"><p class="faq-q">Q. AdSenseとAmazon アソシエイトは同時に使えますか？</p><p class="faq-a">使えます。同じページにAdSenseの広告とAmazon アソシエイトのリンクを設置することはGoogleポリシー上問題ありません。</p></div>
<div class="faq-item"><p class="faq-q">Q. GitHub PagesのサイトでAdSense審査は通りますか？</p><p class="faq-a">通ります。ホスティング先がGitHub PagesかどうかはAdSenseの審査に影響しません。コンテンツの質と量が審査基準です。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="amazon-associates.html">Amazon アソシエイトに登録してみた｜審査通過までに確認したこと</a></div>
<div class="related-item"><a href="github-pages-vs-note.html">なぜnoteじゃなくてGitHub Pagesにしたか｜AdSenseを使いたかった</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)
print("記事2: adsense-application.html 生成完了")


# ============================================================
# 記事3: amazon-associates.html
# ============================================================
articles['amazon-associates'] = build(
    slug='amazon-associates',
    title='Amazon アソシエイトに登録してみた｜審査通過までに確認したこと',
    desc='Amazon アソシエイトに個人ブログで登録した記録です。申請条件・審査基準・180日ルール・初回売上までの流れと、商品リンクの貼り方をまとめました。',
    keywords='Amazon アソシエイト 申請,Amazon Associates 個人ブログ,アマゾン アフィリエイト 始め方',
    og_desc='Amazon アソシエイトに個人ブログで登録した記録。申請条件・180日ルール・商品リンクの貼り方をまとめました。',
    month='3',
    faq_ld=[
        ('Amazon アソシエイトの申請条件は何ですか？', '18歳以上であること、申請時にウェブサイトやSNSのアカウントが必要です。Amazonが特に重視するのはサイトのコンテンツ品質です。スパム的なサイトや薄いコンテンツのサイトは審査で落ちることがあります。'),
        ('Amazon アソシエイトの180日ルールとは何ですか？', '登録後180日以内に3件以上の売上（購入）が発生しないとアカウントが停止されるルールです。停止後は再申請が可能ですが、最初の180日間は積極的に商品リンクを設置することをおすすめします。'),
        ('Amazon アソシエイトの報酬率はどれくらいですか？', 'カテゴリによって異なります。ファッションは10%、家電・カメラは2〜3%、書籍は3%程度が目安です。紹介した商品と異なるカテゴリの商品が購入された場合も報酬が発生します。'),
        ('個人ブログへの商品リンクの貼り方は？', 'Amazon アソシエイト管理画面の「商品リンク」からASIN（商品コード）を入力するか、サイトストライプ機能（Amazonの商品ページ上に表示されるバー）でリンクを取得できます。テキストリンク・画像リンク・テキスト+画像の3種類から選べます。'),
        ('AdSenseとAmazon アソシエイトを同時に使っても問題ありませんか？', '問題ありません。どちらもGoogleのポリシー上、同じページへの設置が認められています。記事の内容に合わせて使い分けると収益効率が上がります。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>Amazon アソシエイトの申請条件と審査の流れ</li>
<li>知らないと困る「180日ルール」の対処法</li>
<li>商品リンクの3種類と貼り方</li>
<li>報酬率の目安とカテゴリ別の違い</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログにAmazon アソシエイトのリンクを設置するために登録した際の記録をまとめておきます。申請前に気になっていた「180日ルール」についても書きました。</p>

<h2>Amazon アソシエイトとは</h2>

<p>Amazon アソシエイトは、Amazonの商品ページへのリンクを自分のサイトに設置し、そのリンク経由で購入が発生した場合に報酬を受け取れるアフィリエイトプログラムです。カメラ・SDカード・レタッチソフトなど、このブログのテーマに関連する商品を紹介できるため申請しました。</p>

<h2>申請手順</h2>

<p><a href="https://affiliate.amazon.co.jp/" target="_blank" rel="noopener noreferrer">Amazon アソシエイト</a>のサイトから申請します。手順は次の通りです。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>Amazonアカウントでログイン（専用アカウントでなく通常のAmazonアカウントでOK）</li>
<li>ウェブサイトのURLとサイトの概要を入力</li>
<li>どんな商品を紹介するか、どのようにAmazonのリンクを使うかを回答</li>
<li>報酬の受け取り方法と税務情報を設定</li>
<li>申請完了、仮承認でリンク作成が可能になる</li>
</ol>

<p>申請後すぐに仮承認状態になり、商品リンクの作成が開始できます。本承認は180日以内に3件の売上が発生することで完了します。</p>

<h2>知っておきたい「180日ルール」</h2>

<p>Amazon アソシエイトには、登録から180日以内に3件以上の売上（Amazonでの購入）を発生させる必要があるというルールがあります。これを達成できなかった場合、アカウントが停止されます（再申請は可能）。</p>

<p>このルールへの対策として、登録後すぐにいくつかの記事に商品リンクを設置しました。SDカードの選び方記事やカメラ紹介記事など、購入につながりやすい記事から優先して商品リンクを入れていきました。</p>

<div class="warn-box">
<p><strong>注意：</strong>「3件の売上」は自分でリンクを踏んで購入しても条件を満たしません。自己購入での条件クリアは規約違反になるため、コンテンツの力で達成する必要があります。</p>
</div>

<h2>商品リンクの貼り方</h2>

<h3>テキストリンク</h3>
<p>「SanDisk 64GB SDカード」のような文章の一部にリンクを張る形式です。自然な文脈でリンクを入れやすく、記事の読みやすさを損ないません。</p>

<h3>画像リンク</h3>
<p>商品画像をリンクにする形式です。視覚的に目立つため、おすすめ商品を紹介する際に使いやすいです。</p>

<h3>テキスト+画像リンク</h3>
<p>商品名と画像を組み合わせたカードタイプです。商品を紹介する際に最もクリックされやすいと言われています。</p>

<h2>報酬率の目安</h2>

<table class="spec-table">
<tr><th>カテゴリ</th><th>報酬率の目安</th></tr>
<tr><td>ファッション・シューズ</td><td>10%</td></tr>
<tr><td>書籍・Kindle</td><td>3〜4%</td></tr>
<tr><td>カメラ・家電</td><td>2〜3%</td></tr>
<tr><td>食品・飲料</td><td>2%</td></tr>
<tr><td>ソフトウェア・PCゲーム</td><td>3〜5%</td></tr>
</table>

<p>カメラやSDカードは単価が高い一方で報酬率は低めです。書籍系は報酬率が比較的高く、1冊あたりの単価が低くても積み重なると収益になります。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. Amazon アソシエイトの申請条件は何ですか？</p><p class="faq-a">18歳以上であること、申請時にウェブサイトやSNSアカウントが必要です。Amazonが特に重視するのはサイトのコンテンツ品質です。スパム的なサイトや薄いコンテンツのサイトは審査で落ちることがあります。</p></div>
<div class="faq-item"><p class="faq-q">Q. Amazon アソシエイトの180日ルールとは何ですか？</p><p class="faq-a">登録後180日以内に3件以上の売上が発生しないとアカウントが停止されるルールです。停止後は再申請が可能ですが、最初の180日間は積極的に商品リンクを設置することをおすすめします。</p></div>
<div class="faq-item"><p class="faq-q">Q. Amazon アソシエイトの報酬率はどれくらいですか？</p><p class="faq-a">カテゴリによって異なります。ファッションは10%、家電・カメラは2〜3%、書籍は3〜4%程度が目安です。紹介した商品と異なるカテゴリの商品が購入された場合も報酬が発生します。</p></div>
<div class="faq-item"><p class="faq-q">Q. AdSenseとAmazon アソシエイトを同時に使っても問題ありませんか？</p><p class="faq-a">問題ありません。どちらも同じページへの設置が認められています。記事の内容に合わせて使い分けると収益効率が上がります。</p></div>
<div class="faq-item"><p class="faq-q">Q. 個人ブログへの商品リンクの貼り方は？</p><p class="faq-a">Amazon アソシエイト管理画面の「商品リンク」からASINを入力するか、サイトストライプ機能でリンクを取得できます。テキストリンク・画像リンク・テキスト+画像の3種類から選べます。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="adsense-application.html">個人ブログにGoogle AdSenseを申請してみた｜審査から承認までの記録</a></div>
<div class="related-item"><a href="github-pages-vs-note.html">なぜnoteじゃなくてGitHub Pagesにしたか｜AdSenseを使いたかった</a></div>
<div class="related-item"><a href="sd-card.html">SDカードの選び方｜カメラ用スペックと失敗しない買い方まとめ</a></div>
</div>
</div>"""
)
print("記事3: amazon-associates.html 生成完了")


# ============================================================
# 記事4: search-console-ctr.html
# ============================================================
articles['search-console-ctr'] = build(
    slug='search-console-ctr',
    title='記事のタイトルを変えたらCTRが動いた話｜サーチコンソール実録',
    desc='Search ConsoleでCTRが低い記事を特定し、タイトルを変更した記録です。8位表示でCTR 0.23%だった記事がタイトル変更でどう変わったか。判断基準と変更後の確認方法をまとめました。',
    keywords='サーチコンソール CTR改善,タイトル変更 SEO,クリック率 上げる,Search Console 使い方',
    og_desc='Search Consoleで8位表示なのにCTR 0.23%だった記事のタイトルを変えた記録。判断基準と変更後の確認方法をまとめました。',
    month='3',
    faq_ld=[
        ('検索順位8位のCTRの目安は何%ですか？', '検索順位8位のCTRは一般的に2〜4%程度が目安と言われています。1%を下回る場合は、タイトルや検索意図との乖離が疑われます。ただし業種・キーワードによって大きく異なるため、自分のサイトの平均CTRと比較して判断することをおすすめします。'),
        ('タイトル変更がSEOに与える影響は？', 'タイトルを変更すると検索結果での表示が変わり、CTRに影響します。変更後1〜2週間でGoogleがクロールして新しいタイトルが検索結果に反映されます。タイトルに検索ニーズと一致するキーワードが含まれると、CTRが改善されることが多いです。ただしtitle変更が検索順位に影響する場合もあるため、大幅に変更しすぎないことがポイントです。'),
        ('Search ConsoleでCTRを確認する方法は？', 'Search Consoleの「検索パフォーマンス」→「ページ」タブで各記事のCTRを確認できます。CTRが低いページを特定したら「クエリ」タブに切り替えて、そのページに実際にどのキーワードで表示されているかを確認しましょう。'),
        ('タイトルを変更したらインデックス再登録は必要ですか？', 'タイトル変更だけであれば手動でのインデックス再登録は必ずしも必要ではありません。Googleは定期的にクロールして自動的に更新します。早く反映させたい場合はSearch ConsoleのURL検査からインデックス登録をリクエストできます。'),
        ('CTRを上げるタイトルの書き方のポイントは？', '検索キーワードをタイトルの前半に入れること、具体的な数字を入れること（例：「7選」「2026年版」）、疑問形や比較形式を使うことが効果的です。また「まとめ」より「比較」「方法」「違い」の方がクリックされやすい傾向があります。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>Search ConsoleでCTRが低い記事を特定する方法</li>
<li>タイトル変更の判断基準（順位とCTRの組み合わせ）</li>
<li>実際に変更した記事と変更内容</li>
<li>変更後の確認方法と待ち時間の目安</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログのSearch Consoleを見ていて気になることがありました。ある記事が検索結果の8位前後に表示されているのに、クリック率（CTR）が0.23%しかない、という状態が続いていたんです。</p>

<h2>「順位は良いのにクリックされない」の意味</h2>

<p>Search Consoleで確認したところ、Exifの記事が3ヶ月間で1,318回表示されていたにもかかわらず、クリック数はわずか3回でした。掲載順位は8.4位。8位前後なら通常2〜4%程度のCTRが期待できるはずなのに、0.23%はかなり低い数字です。</p>

<p>この状況が意味するのは、<strong>Googleは記事を良いコンテンツと判断して上位に置いているが、タイトルや説明文が検索した人の期待と合っていないためクリックされていない</strong>ということです。コンテンツの問題ではなく、見せ方の問題です。</p>

<h2>どのキーワードで表示されていたか</h2>

<p>Search Consoleのクエリデータでこのページへのアクセスを絞り込むと、上位クエリは「x 画像 位置情報を含む」「x 写真 位置情報を含む」でした。つまりユーザーは「X（Twitter）に投稿すると位置情報が残るのか？」という疑問を持って検索していたのです。</p>

<p>一方、変更前のタイトルは「写真のExif情報とは？位置情報のリスクと削除方法まとめ」でした。このタイトルは「Exif情報の解説」を求めている人向けで、「Xに投稿すると位置情報が残るか？」という疑問を持つ人には響きにくいです。</p>

<h2>タイトル変更の判断基準</h2>

<p>タイトル変更を検討する条件はシンプルです。</p>

<table class="spec-table">
<tr><th>状態</th><th>対応</th></tr>
<tr><td>順位10位以内・CTR 2%以上</td><td>変更不要（順調）</td></tr>
<tr><td>順位10位以内・CTR 1%未満</td><td>タイトル変更を検討</td></tr>
<tr><td>順位11〜20位・CTR問わず</td><td>コンテンツ強化が先</td></tr>
<tr><td>順位21位以下</td><td>タイトル変更より記事のリライトが先</td></tr>
</table>

<p>ポイントは「順位が良いのにCTRが低い記事」をターゲットにすることです。順位が低い場合はタイトル変更よりも記事の中身を改善する方が先です。</p>

<h2>実際に変更したタイトル</h2>

<p>Exif記事のタイトルを次のように変更しました。</p>

<div class="point-box">
<p><strong>変更前：</strong>写真のExif情報とは？位置情報のリスクと削除方法まとめ【2026年版】</p>
<p><strong>変更後：</strong>X（Twitter）に写真の位置情報は残る？Exif確認・削除方法まとめ</p>
</div>

<p>変更のポイントは2つです。まず「X（Twitter）」をタイトルの先頭に持ってきました。検索ユーザーが知りたいことを最初に示すことでクリック率が上がります。次に「【2026年版】」を削除して38文字以内に収めました。検索結果で途中で切れないタイトル長の目安は40文字以内です。</p>

<h2>変更後の確認と待ち時間</h2>

<p>タイトルを変更してHTMLをアップロードしたあと、Search ConsoleのURL検査から「インデックス登録をリクエスト」しました。Googleが新しいタイトルを認識して検索結果に反映されるまで通常1〜2週間かかります。</p>

<p>変更から2週間以上経ったら、Search Consoleで以下を確認します。</p>
<ul style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>CTRが上昇しているか</li>
<li>クリック数が増えているか</li>
<li>掲載順位に大きな変化がないか（タイトル変更で順位が下がる場合がある）</li>
</ul>

<p>タイトル変更は手軽にできる施策ですが、やりすぎると逆効果になることもあります。1本変更したら様子を見てから次に進む、というペースが安全です。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. 検索順位8位のCTRの目安は何%ですか？</p><p class="faq-a">検索順位8位のCTRは一般的に2〜4%程度が目安と言われています。1%を下回る場合は、タイトルや検索意図との乖離が疑われます。ただし業種・キーワードによって大きく異なるため、自分のサイトの平均CTRと比較して判断することをおすすめします。</p></div>
<div class="faq-item"><p class="faq-q">Q. タイトル変更がSEOに与える影響は？</p><p class="faq-a">変更後1〜2週間でGoogleがクロールして新しいタイトルが反映されます。タイトルに検索ニーズと一致するキーワードが含まれると、CTRが改善されることが多いです。ただしtitle変更が検索順位に影響する場合もあるため、大幅に変更しすぎないことがポイントです。</p></div>
<div class="faq-item"><p class="faq-q">Q. Search ConsoleでCTRを確認する方法は？</p><p class="faq-a">「検索パフォーマンス」→「ページ」タブで各記事のCTRを確認できます。CTRが低いページを特定したら「クエリ」タブに切り替えて、実際にどのキーワードで表示されているかを確認しましょう。</p></div>
<div class="faq-item"><p class="faq-q">Q. CTRを上げるタイトルの書き方のポイントは？</p><p class="faq-a">検索キーワードをタイトルの前半に入れること、具体的な数字を含めること（「7選」「2026年版」等）、疑問形や比較形式を使うことが効果的です。また「まとめ」より「比較」「方法」「違い」の方がクリックされやすい傾向があります。</p></div>
<div class="faq-item"><p class="faq-q">Q. タイトル変更後のインデックス再登録は必要ですか？</p><p class="faq-a">タイトル変更だけであれば必須ではありません。早く反映させたい場合はSearch ConsoleのURL検査から「インデックス登録をリクエスト」できます。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="search-console-basics.html">サーチコンソールの見方を覚えた備忘録｜表示回数・CTR・掲載順位</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
<div class="related-item"><a href="google-index-not-found.html">Googleにインデックスされるまで｜サイトマップ送信からの記録</a></div>
</div>
</div>"""
)
print("記事4: search-console-ctr.html 生成完了")


# ============================================================
# 記事5: search-console-basics.html
# ============================================================
articles['search-console-basics'] = build(
    slug='search-console-basics',
    title='サーチコンソールの見方を覚えた備忘録｜表示回数・CTR・掲載順位',
    desc='Google Search Consoleの基本的な見方をまとめた備忘録です。表示回数・クリック数・CTR・掲載順位の意味と読み方、サイトマップ送信、インデックス確認の手順を初心者向けに解説しています。',
    keywords='サーチコンソール 使い方,Search Console 見方,表示回数 クリック率 違い,サイトマップ 送信',
    og_desc='Google Search Consoleの表示回数・CTR・掲載順位の読み方とサイトマップ送信の手順をまとめた備忘録です。',
    month='3',
    faq_ld=[
        ('Google Search Consoleは無料で使えますか？', '完全無料で使えます。Googleアカウントがあれば誰でも利用でき、ウェブサイトの所有権を確認するだけで使い始められます。'),
        ('Search ConsoleとGoogle Analyticsの違いは何ですか？', 'Search Consoleは「Googleからサイトがどう見られているか」を確認するツールです。検索キーワード・表示回数・CTR・掲載順位など、検索エンジン経由の情報が主です。Google Analyticsは「サイトに来たユーザーが何をしたか」を分析するツールです。ページビュー・滞在時間・離脱率など、サイト内の行動データを計測します。両方を使うとより精度の高い分析ができます。'),
        ('Search Consoleで「URL がGoogleに登録されていません」と表示された場合は？', 'まだGoogleにクロールされていない状態です。URL検査画面で「インデックス登録をリクエスト」ボタンを押してください。リクエスト後、1〜2週間でクロールされることが多いです。'),
        ('掲載順位の平均が10位以下でも改善できますか？', '改善できます。掲載順位10〜20位の記事は、タイトルにキーワードを追加する、記事の情報量を増やす、内部リンクを充実させるなどの対策が有効です。ただし即効性はなく、変更後2〜4週間で効果を確認するのが現実的です。'),
        ('サイトマップとは何ですか？なぜ必要ですか？', 'サイトマップ（sitemap.xml）はサイト内のすべてのURLをまとめたXMLファイルです。GoogleのクローラーがサイトのURL構造を把握しやすくなるため、インデックスが早まる効果があります。Search Consoleからサイトマップを送信することで、Googleに「このURLもクロールしてください」と伝えられます。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>Search Consoleの登録手順（所有権確認まで）</li>
<li>「表示回数」「クリック数」「CTR」「掲載順位」それぞれの意味</li>
<li>サイトマップの送信手順</li>
<li>AnalyticsとSearch Consoleの使い分け</li>
</ul>
</div>

<p>こんにちは、ツバサです。ブログを始めてからしばらくはSearch Consoleの見方がよくわかっていませんでした。どの数字が何を意味するのか、何を確認すればいいのかを調べてまとめた備忘録です。</p>

<h2>Search Consoleとは何か</h2>

<p>Google Search Console（サーチコンソール）は、自分のサイトがGoogle検索でどのように表示されているかを確認できる無料ツールです。「どのキーワードで表示されているか」「何位に表示されているか」「クリックされているか」をページ単位・キーワード単位で確認できます。</p>

<p>Google Analyticsがサイトに来た人の行動を分析するのに対して、Search Consoleは「Googleからサイトがどう見られているか」を確認するツールです。両方使うとより正確な分析ができますが、まずSearch Consoleから始めるのがおすすめです。</p>

<h2>登録と所有権確認の手順</h2>

<p><a href="https://search.google.com/search-console/" target="_blank" rel="noopener noreferrer">Google Search Console</a>にGoogleアカウントでログインし、「URLプレフィックス」にサイトのURLを入力します。所有権の確認方法はいくつかありますが、HTMLファイルをサイトに設置する方法が最も簡単です。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>「HTMLファイル」を選択してファイルをダウンロード</li>
<li>ファイルをサイトのルートディレクトリにアップロード</li>
<li>Search Consoleに戻って「確認」ボタンをクリック</li>
</ol>

<p>確認が完了すると、Search Consoleにサイトのデータが表示されるようになります。ただしデータが集まるまで数日〜1週間かかります。</p>

<h2>「検索パフォーマンス」の4つの数字</h2>

<h3>表示回数（Impressions）</h3>
<p>検索結果にページが表示された回数です。クリックされなくても、検索結果の画面に出ただけでカウントされます。表示回数が多いのにクリックが少ない場合は、タイトルや内容が検索者の期待と合っていない可能性があります。</p>

<h3>クリック数（Clicks）</h3>
<p>検索結果からサイトへのクリック数です。実際にページを訪問した人数に相当します。</p>

<h3>CTR（Click Through Rate：クリック率）</h3>
<p>「クリック数 ÷ 表示回数 × 100」で計算されます。掲載順位1位のCTRは20〜30%程度、10位は1〜2%程度が目安とされています。同じ順位でも記事によってCTRは大きく変わります。CTRが低い場合はタイトルの見直しが有効です。</p>

<h3>掲載順位（Position）</h3>
<p>検索結果での平均表示位置です。1位が最上位で、数字が大きいほど下位です。10以内に入ると検索結果の1ページ目に表示されます。</p>

<h2>サイトマップの送信</h2>

<p>Search Consoleの左メニュー「サイトマップ」からsitemap.xmlのURLを入力して送信します。サイトマップが正しく読み込まれると「成功しました」と表示されます。</p>

<p>サイトマップを送信するとGoogleのクローラーがサイトの全URLを認識しやすくなり、インデックス登録が早まることが多いです。ブログを始めたらまず送信しておくことをおすすめします。</p>

<h2>URL検査でインデックスを確認する</h2>

<p>Search Consoleの上部の検索バーにURLを入力すると、そのページのインデックス状況を確認できます。「URLはGoogleに登録されています」と表示されれば検索結果に出る状態です。「URLがGoogleに登録されていません」と表示された場合は「インデックス登録をリクエスト」ボタンを押してクロールを促せます。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. Google Search Consoleは無料で使えますか？</p><p class="faq-a">完全無料で使えます。Googleアカウントがあれば誰でも利用でき、ウェブサイトの所有権を確認するだけで使い始められます。</p></div>
<div class="faq-item"><p class="faq-q">Q. Search ConsoleとGoogle Analyticsの違いは何ですか？</p><p class="faq-a">Search Consoleは「Googleからサイトがどう見られているか」を確認するツールです（検索キーワード・表示回数・CTR・順位）。Google Analyticsは「サイトに来たユーザーが何をしたか」を分析するツールです（PV・滞在時間・離脱率）。両方を使うとより精度の高い分析ができます。</p></div>
<div class="faq-item"><p class="faq-q">Q. サイトマップとは何ですか？なぜ必要ですか？</p><p class="faq-a">サイトマップ（sitemap.xml）はサイト内の全URLをまとめたXMLファイルです。GoogleのクローラーがサイトのURL構造を把握しやすくなるため、インデックスが早まる効果があります。</p></div>
<div class="faq-item"><p class="faq-q">Q. CTR（クリック率）の目安は何%ですか？</p><p class="faq-a">掲載順位1位で20〜30%、5位で5〜8%、10位で1〜2%程度が一般的な目安です。同じ順位でもキーワードや記事によって大きく変わります。</p></div>
<div class="faq-item"><p class="faq-q">Q. 「URLがGoogleに登録されていません」と表示された場合は？</p><p class="faq-a">まだGoogleにクロールされていない状態です。URL検査画面で「インデックス登録をリクエスト」ボタンを押してください。リクエスト後、1〜2週間でクロールされることが多いです。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="search-console-ctr.html">記事のタイトルを変えたらCTRが動いた話｜サーチコンソール実録</a></div>
<div class="related-item"><a href="google-index-not-found.html">Googleにインデックスされるまで｜サイトマップ送信からの記録</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)
print("記事5: search-console-basics.html 生成完了")


# ============================================================
# 記事6: blog-seo-basics.html
# ============================================================
articles['blog-seo-basics'] = build(
    slug='blog-seo-basics',
    title='個人ブログを始めてSEOを勉強した記録｜最初にやること5つ',
    desc='個人ブログのSEO対策として最初にやった5つのことをまとめました。タイトル・description・サイトマップ・構造化データ・内部リンクの基本を、ブログ運営初心者の視点で記録しています。',
    keywords='個人ブログ SEO 始め方,ブログ SEO 初心者,タイトル description 書き方,サイトマップ 設置',
    og_desc='個人ブログのSEO対策として最初にやった5つのこと。タイトル・description・サイトマップ・構造化データ・内部リンクの基本をまとめました。',
    month='3',
    faq_ld=[
        ('個人ブログのSEOで一番効果的な対策は何ですか？', '一番効果的なのはタイトルタグの最適化です。検索キーワードをタイトルの前半に含め、32〜40文字に収めることで、検索結果でのクリック率が上がります。次にmeta descriptionを110〜125文字で丁寧に書くことが重要です。これらはページのコンテンツを変えずにできる施策なので、まず取り組む価値があります。'),
        ('個人ブログがGoogleに評価されるまでどれくらいかかりますか？', '一般的に3〜6ヶ月は必要です。新規ドメイン・サイトはGoogleからの信頼を得るまで時間がかかります。継続的に記事を追加し、各記事の質を高めることで少しずつ評価が上がっていきます。'),
        ('meta descriptionは検索順位に直接影響しますか？', 'Googleはmeta descriptionを検索順位の直接的な要因としていないと公表しています。ただし検索結果に表示されるスニペットに影響するため、クリック率（CTR）に間接的に影響します。CTRが上がると間接的に順位改善につながる場合があります。'),
        ('内部リンクとは何ですか？なぜ重要なのですか？', '内部リンクは同じサイト内のページへのリンクです。内部リンクを充実させるとGoogleのクローラーがサイト全体を効率よく把握できるようになります。また、関連記事へのリンクを入れることで読者の回遊率が上がり、サイト全体の評価にプラスに働くとされています。'),
        ('構造化データ（JSON-LD）とは何ですか？', '構造化データは、ページの内容を機械が読みやすい形式で表現したコードです。FAQページのJSON-LDを設置すると、検索結果に「よくある質問」の展開ボックスが表示されることがあります。クリック率の向上と、AIへの情報伝達（LLMO）の両方に効果があります。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>タイトルタグとmeta descriptionの書き方の基本</li>
<li>サイトマップとrobots.txtの役割と設置方法</li>
<li>FAQ構造化データ（JSON-LD）とは何か</li>
<li>内部リンクの考え方</li>
<li>SEO施策の優先順位のつけ方</li>
</ul>
</div>

<p>こんにちは、ツバサです。ブログを始めたとき「SEO対策をやらないといけない」とは聞いていたけど、何から手をつければいいかわかりませんでした。調べながら実際にやってみたことを順番に書いておきます。</p>

<h2>1. タイトルタグを32〜40文字に収める</h2>

<p>タイトルタグ（&lt;title&gt;タグ）は検索結果の見出しとして表示される最も重要な要素です。長すぎると検索結果で途中で切れてしまいます。</p>

<p>Googleの検索結果でタイトルが切れないのは全角32〜40文字程度が目安です（スマホだと少し短め）。最初は記事のタイトルをそのまま使っていたら40字を超えることが多く、後から短くし直す作業が発生しました。最初からこの制限を意識して書く習慣をつけた方が楽です。</p>

<p>また、検索されたいキーワードをタイトルの<strong>前半</strong>に入れることが重要です。「SDカードの選び方メモ｜カメラ用に必要な〜」より「SDカードの選び方｜カメラ用スペックと〜」の方がキーワードが先に来て効果的です。</p>

<h2>2. meta descriptionを110〜125文字で書く</h2>

<p>meta descriptionは検索結果のタイトル下に表示される説明文です。Googleが検索結果に表示するスニペットに使われることが多いです（必ずしも使われるわけではありませんが）。</p>

<p>最初は80〜90文字で書いていることが多く、後から確認したら全記事の8割以上が100文字未満でした。110〜125文字を目標に、記事内の具体的な数値やサービス名を含めて書くようにしています。</p>

<div class="warn-box">
<p><strong>注意：</strong>135文字を超えると検索結果で途中で切れます。長すぎず短すぎず、110〜125文字が安全な範囲です。</p>
</div>

<h2>3. sitemap.xmlとrobots.txtを設置する</h2>

<p>sitemap.xmlはサイト内の全URLをまとめたXMLファイルです。GoogleのクローラーにサイトのURL構造を伝えるために設置します。Search Consoleからsitemap.xmlのURLを送信すると、クロールが早くなる効果があります。</p>

<p>robots.txtはクローラーに「このページはクロールしないで」と指示するためのファイルです。サイトマップのURLを記述しておくと、クローラーがサイトマップを見つけやすくなります。</p>

<h2>4. FAQ構造化データ（JSON-LD）を全記事に入れる</h2>

<p>構造化データはページの内容を機械が読みやすい形式で表現したコードです。FAQページのJSON-LDを設置すると、Googleの検索結果に「よくある質問」のボックスが表示されることがあります。</p>

<p>構造化データを入れた後からの変化として、検索結果の表示が変わった記事があります（全部ではない）。またFAQ形式の構造化データは、ChatGPTやClaudeなどのAIが記事を引用する際に参照されやすいという効果もあると言われています。</p>

<h2>5. 内部リンクを記事間に入れる</h2>

<p>同じサイト内の関連記事へのリンク（内部リンク）を記事の本文や末尾に入れることで、GoogleのクローラーがサイトのURL構造を把握しやすくなります。また読者が関連記事を読み続けてくれる効果もあります。</p>

<p>内部リンクのアンカーテキスト（リンクになっている文字）は「こちら」ではなく、リンク先の内容を具体的に示すテキストにすることがポイントです。「SDカードの選び方記事はこちら」より「<a href="sd-card.html">SDカードの選び方まとめ</a>」の方が効果的です。</p>

<h2>施策の優先順位</h2>

<table class="spec-table">
<tr><th>施策</th><th>効果</th><th>工数</th><th>優先度</th></tr>
<tr><td>タイトル最適化</td><td>高</td><td>低</td><td>★★★</td></tr>
<tr><td>meta description改善</td><td>中（CTR経由）</td><td>低</td><td>★★★</td></tr>
<tr><td>sitemap.xml設置</td><td>中</td><td>低</td><td>★★★</td></tr>
<tr><td>FAQ構造化データ</td><td>中</td><td>中</td><td>★★</td></tr>
<tr><td>内部リンク整備</td><td>中</td><td>中</td><td>★★</td></tr>
<tr><td>記事のリライト</td><td>高</td><td>高</td><td>★（後回し）</td></tr>
</table>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. 個人ブログのSEOで一番効果的な対策は何ですか？</p><p class="faq-a">タイトルタグの最適化が最も効果的です。検索キーワードをタイトルの前半に含め、32〜40文字に収めることでクリック率が上がります。次にmeta descriptionを110〜125文字で丁寧に書くことが重要です。</p></div>
<div class="faq-item"><p class="faq-q">Q. 個人ブログがGoogleに評価されるまでどれくらいかかりますか？</p><p class="faq-a">一般的に3〜6ヶ月は必要です。新規ドメイン・サイトはGoogleからの信頼を得るまで時間がかかります。継続的に記事を追加し、各記事の質を高めることで少しずつ評価が上がっていきます。</p></div>
<div class="faq-item"><p class="faq-q">Q. meta descriptionは検索順位に直接影響しますか？</p><p class="faq-a">Googleはmeta descriptionを検索順位の直接的な要因としていないと公表しています。ただし検索結果のスニペットに影響するため、CTRに間接的に影響します。</p></div>
<div class="faq-item"><p class="faq-q">Q. 構造化データ（JSON-LD）とは何ですか？</p><p class="faq-a">ページの内容を機械が読みやすい形式で表現したコードです。FAQページのJSON-LDを設置すると、検索結果に「よくある質問」の展開ボックスが表示されることがあります。SEOとLLMO（AIへの最適化）の両方に効果があります。</p></div>
<div class="faq-item"><p class="faq-q">Q. 内部リンクとは何ですか？なぜ重要なのですか？</p><p class="faq-a">内部リンクは同じサイト内のページへのリンクです。GoogleのクローラーがサイトのURL構造を把握しやすくなり、関連記事への誘導で読者の回遊率も上がります。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="search-console-basics.html">サーチコンソールの見方を覚えた備忘録｜表示回数・CTR・掲載順位</a></div>
<div class="related-item"><a href="faq-structured-data.html">記事にFAQ構造化データを入れると検索結果がどう変わるか調べた</a></div>
<div class="related-item"><a href="llmo-article-writing.html">AIに答えてもらいやすい記事の書き方を調べた｜LLMOって何？</a></div>
</div>
</div>"""
)
print("記事6: blog-seo-basics.html 生成完了")


# ============================================================
# 記事7: llmo-article-writing.html
# ============================================================
articles['llmo-article-writing'] = build(
    slug='llmo-article-writing',
    title='AIに答えてもらいやすい記事の書き方を調べた｜LLMOって何？',
    desc='LLMO（LLM Optimization）とは何か、SEOとの違い、AIに引用されやすい記事を書くために有効なFAQ構造化データ・llms.txt・記事冒頭の要約セクションについて調べた備忘録です。',
    keywords='LLMO とは,LLM Optimization,AIに引用される 記事,llms.txt 個人ブログ',
    og_desc='LLMO（LLM Optimization）の概念とFAQ構造化データ・llms.txtの効果をブログ運営者目線で調べた備忘録です。',
    month='3',
    faq_ld=[
        ('LLMOとSEOの違いは何ですか？', 'SEOはGoogle・Bingなどの検索エンジンで上位表示されるための最適化です。LLMOはChatGPT・Claude・Geminiなどの大規模言語モデル（LLM）に記事を正しく引用・参照されるための最適化です。検索エンジンはURLをインデックスして順位付けしますが、LLMは学習データやRAG（検索拡張生成）を通じてコンテンツを取得します。'),
        ('LLMOに効果的な記事構造はありますか？', 'FAQ形式とJSON-LD構造化データの組み合わせが効果的とされています。LLMはFAQ形式の「Q&A」構造を引用しやすい傾向があります。また記事冒頭に「この記事でわかること」として箇条書きで要点をまとめることで、LLMが記事の内容を要約して回答する際の精度が上がります。'),
        ('llms.txtとは何ですか？', 'llms.txtはサイトのルートに置くMarkdown形式のファイルで、LLMにサイトの構造と記事一覧を伝えるためのものです。robots.txtがクローラーへの指示書であるのに対し、llms.txtはLLMへの情報提供ファイルです。まだ業界標準ではありませんが、AnthropicやOpenAIが対応を進めており、設置しておいて損はない施策です。'),
        ('個人ブログでもLLMOに取り組む意味はありますか？', 'あります。ChatGPTやClaudeに「〜のおすすめサービスを教えて」と質問するユーザーが増えており、AIの回答に自分のサイトや紹介しているサービスが含まれる可能性があります。特にニッチなトピックや比較記事は、LLMが引用しやすいコンテンツです。'),
        ('LLMO対策として今すぐできることは何ですか？', '今すぐできる対策は3つです。①全記事にFAQ構造化データ（JSON-LD）を設置する。②記事の冒頭に「この記事でわかること」として要点を箇条書きで書く。③llms.txtをサイトルートに設置して記事一覧とサービス情報を記載する。これらはいずれもHTMLの修正だけで対応できます。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>LLMOとは何か・SEOとの違い</li>
<li>ChatGPTやClaudeに引用されやすい記事構造</li>
<li>FAQ構造化データとllms.txtの効果と設置方法</li>
<li>個人ブログでLLMOに取り組む意味</li>
</ul>
</div>

<p>こんにちは、ツバサです。SEO対策を調べているうちに「LLMO」という言葉を見かけるようになりました。ChatGPTやClaudeに質問すると記事が引用されやすくなる、という話で、ブログ運営者として気になったので調べた内容をまとめておきます。</p>

<h2>LLMOとは何か</h2>

<p>LLMO（Large Language Model Optimization）は、ChatGPT・Claude・Geminiなどの大規模言語モデル（LLM）に自分のコンテンツを正しく認識・引用されるための最適化です。</p>

<p>SEOがGoogleやBingの検索エンジンを対象にしているのに対し、LLMOはAIチャットボットを対象にしています。「レタッチサービスのおすすめを教えて」とChatGPTに質問したとき、自分のブログで紹介したサービスが回答に含まれるかどうか、という文脈です。</p>

<h2>LLMに引用されやすい記事の構造</h2>

<h3>FAQ形式＋JSON-LD構造化データ</h3>
<p>LLMはFAQ形式の「Q&A」構造を引用しやすいとされています。「Q. ○○とは何ですか？」「A. ○○とは〜です」という形式は、LLMが回答を生成する際に参照しやすいためです。さらにJSON-LDのFAQPage schemaを設置することで、構造化された形でページの内容をLLMに伝えられます。</p>

<h3>記事冒頭の要約セクション</h3>
<p>記事の先頭に「この記事でわかること」として要点を箇条書きで書くと、LLMが記事を要約して回答する際の精度が上がります。LLMが記事を参照する際に最初に読む部分が最も引用されやすいためです。</p>

<h3>具体的な数値・サービス名・固有名詞を含める</h3>
<p>「安い」ではなく「1枚300円〜」、「アプリ」ではなく「Snapseed・TouchRetouch」のように、具体的な情報を含めることでLLMが回答に使いやすい情報になります。</p>

<h2>llms.txtとは何か</h2>

<p>llms.txtはサイトのルートに置くMarkdown形式のファイルで、LLMにサイトの構造と記事一覧を伝えるための仕組みです。たとえばこのブログの場合、<a href="https://tsubasa-memo.github.io/llms.txt" target="_blank" rel="noopener noreferrer">tsubasa-memo.github.io/llms.txt</a>に設置しています。</p>

<p>robots.txtがGoogleなどのクローラーに「このページはクロールしないで」と指示するファイルであるのに対し、llms.txtはLLMに「このサイトには以下の記事があり、このような情報を提供しています」と伝えるためのファイルです。</p>

<p>まだ業界標準ではなく、すべてのAIが対応しているわけではありません。ただしコストゼロで設置できるため、やっておいて損はない施策です。</p>

<h2>個人ブログでLLMOに取り組む意味</h2>

<p>AI検索が普及すると、Google検索経由のアクセスが減ってAI経由のアクセスが増えていく可能性があります。現時点では個人ブログへのLLMO対策の効果を数値で証明するのは難しいですが、コンテンツの質を高めること・FAQ構造化データを入れること・llms.txtを設置することは、SEOとLLMOの両方に有効な施策です。</p>

<p>特に比較記事（「○○サービスを比較してみた」）や疑問に答える記事（「○○とは何か」）は、LLMが引用しやすいコンテンツとして知られています。レタッチサービスの比較や写真アプリの比較を書いているこのブログのテーマは、LLMOの観点からも相性が良いと考えています。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. LLMOとSEOの違いは何ですか？</p><p class="faq-a">SEOはGoogle・Bingなどの検索エンジンで上位表示されるための最適化です。LLMOはChatGPT・Claude・Geminiなどの大規模言語モデルに記事を正しく引用・参照されるための最適化です。</p></div>
<div class="faq-item"><p class="faq-q">Q. LLMOに効果的な記事構造はありますか？</p><p class="faq-a">FAQ形式とJSON-LD構造化データの組み合わせが効果的です。また記事冒頭に「この記事でわかること」として要点を箇条書きでまとめることで、LLMが記事を要約して回答する際の精度が上がります。</p></div>
<div class="faq-item"><p class="faq-q">Q. llms.txtとは何ですか？</p><p class="faq-a">サイトのルートに置くMarkdown形式のファイルで、LLMにサイトの構造と記事一覧を伝えるためのものです。robots.txtのLLM版のようなイメージです。まだ業界標準ではありませんが、コストゼロで設置できます。</p></div>
<div class="faq-item"><p class="faq-q">Q. LLMO対策として今すぐできることは何ですか？</p><p class="faq-a">①全記事にFAQ構造化データ（JSON-LD）を設置する、②記事の冒頭に「この記事でわかること」を箇条書きで書く、③llms.txtをサイトルートに設置して記事一覧とサービス情報を記載する、の3つが今すぐできる対策です。</p></div>
<div class="faq-item"><p class="faq-q">Q. 個人ブログでもLLMOに取り組む意味はありますか？</p><p class="faq-a">あります。比較記事や疑問に答える記事はLLMが引用しやすいコンテンツです。特にニッチなトピックを扱う個人ブログは、大手サイトよりも専門性が高い場合があり、LLMに参照されるチャンスがあります。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="llms-txt-setup.html">llms.txtとは何か｜AIにブログを読ませるためのファイルを設置した</a></div>
<div class="related-item"><a href="faq-structured-data.html">記事にFAQ構造化データを入れると検索結果がどう変わるか調べた</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)
print("記事7: llmo-article-writing.html 生成完了")


# ============================================================
# 記事8: llms-txt-setup.html
# ============================================================
articles['llms-txt-setup'] = build(
    slug='llms-txt-setup',
    title='llms.txtとは何か｜AIにブログを読ませるためのファイルを設置した',
    desc='llms.txtの仕様・書き方・設置手順をまとめた備忘録です。robots.txtとの違い、どのAIが対応しているか、個人ブログへの設置効果について調べた内容を記録しています。',
    keywords='llms.txt とは,llms.txt 書き方,llms.txt 設置,AI ブログ 最適化',
    og_desc='llms.txtの仕様・書き方・設置手順をまとめた備忘録。robots.txtとの違いと個人ブログへの設置効果について調べました。',
    month='3',
    faq_ld=[
        ('llms.txtとrobots.txtの違いは何ですか？', 'robots.txtはGoogleなどのクローラーに対して「このページはクロールしないで」と指示するファイルです。llms.txtはLLM（大規模言語モデル）に対してサイトの構造や記事一覧を伝えるためのファイルです。目的と対象が異なりますが、どちらもサイトのルートに置きます。'),
        ('llms.txtはすべてのAIに対応していますか？', '2026年時点では対応状況はAIによって異なります。Claude（Anthropic）はllms.txtを参照することが知られています。ChatGPT（OpenAI）やGemini（Google）の対応状況は変化しています。まだ業界標準ではありませんが、設置コストがほぼゼロなのでやっておいて損はありません。'),
        ('llms.txtはどこに設置すればいいですか？', 'サイトのルートに「llms.txt」というファイル名で設置します。GitHub Pagesの場合はリポジトリのルートディレクトリに置くだけです。URLは「https://サイトURL/llms.txt」になります。'),
        ('llms.txtに書くべき内容は何ですか？', 'サイト名・サイトの概要・カテゴリ一覧・記事一覧（タイトルとURL）・運営者情報が基本的な内容です。記事一覧では各記事の説明文を1〜2文で添えると、LLMが記事の内容を把握しやすくなります。'),
        ('llms.txtの設置効果はどうやって確認しますか？', '直接的な効果測定は難しいです。ChatGPTやClaudeに「〔自分のブログのトピック〕について教えて」と質問したとき、自分のブログや紹介しているサービスが回答に含まれるかどうかを定期的に確認する方法が現実的です。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>llms.txtの概要とrobots.txtとの違い</li>
<li>llms.txtの書き方（フォーマット）</li>
<li>GitHub Pagesへの設置手順</li>
<li>対応しているAIと効果の確認方法</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログのSEO・LLMO対策を調べているうちに「llms.txt」というファイルの存在を知りました。設置するだけでAIがブログの内容を把握しやすくなるというので、実際にやってみた記録をまとめます。</p>

<h2>llms.txtとは何か</h2>

<p>llms.txtは、サイトのルートに置くMarkdown形式のファイルです。ChatGPT・Claude・GeminiなどのLLM（大規模言語モデル）に対して、サイトにどんな情報があるかを伝えることを目的としています。</p>

<p>robots.txtがGoogleのクローラーに「このページはクロールしないで」と指示するファイルであるのに対し、llms.txtはLLMに「このサイトには以下の記事があります」と伝えるファイルです。</p>

<p>提唱者はAIツール開発者のJeremy Howardで、2024年に仕様が公開されました。AnthropicはClaudeの<a href="https://docs.anthropic.com/" target="_blank" rel="noopener noreferrer">公式ドキュメント</a>にllms.txtを設置しており、徐々に普及が進んでいます。</p>

<h2>書き方の基本フォーマット</h2>

<p>llms.txtはMarkdown形式で記述します。基本構造は次の通りです。</p>

<div class="point-box">
<pre style="white-space:pre-wrap;font-size:13px;line-height:1.7"># サイト名

&gt; サイトの概要説明（1〜2文）

## カテゴリ

- カテゴリ1：説明
- カテゴリ2：説明

## 記事一覧

- [記事タイトル](URL): 記事の内容を1〜2文で説明

## 運営者

運営者の情報</pre>
</div>

<p>記事一覧は全記事を掲載する必要はありませんが、掲載する記事が多いほどLLMが参照できる情報量が増えます。各記事の説明文には具体的なサービス名・数値・キーワードを含めると、LLMが記事の内容を正確に把握できます。</p>

<h2>GitHub Pagesへの設置手順</h2>

<p>GitHub Pagesの場合、リポジトリのルートに「llms.txt」という名前のファイルを作成してコミットするだけです。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>テキストエディタで上記フォーマットに沿ってllms.txtを作成</li>
<li>リポジトリのルートにファイルを追加してコミット・push</li>
<li>「https://ユーザー名.github.io/llms.txt」にアクセスして内容が表示されることを確認</li>
</ol>

<p>このブログのllms.txtは<a href="https://tsubasa-memo.github.io/llms.txt" target="_blank" rel="noopener noreferrer">こちら</a>で確認できます。</p>

<h2>運用上の注意点</h2>

<p>新しい記事を公開するたびにllms.txtも更新する必要があります。記事一覧が古いままだと、最新の記事がLLMに伝わりません。記事追加のワークフローにllms.txt更新を組み込んでおくのがおすすめです。</p>

<div class="warn-box">
<p><strong>注意：</strong>llms.txtに書いた情報がLLMの回答に即座に反映されるわけではありません。LLMのトレーニングサイクルやRAG（検索拡張生成）の仕組みによって、反映されるタイミングは異なります。</p>
</div>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. llms.txtとrobots.txtの違いは何ですか？</p><p class="faq-a">robots.txtはGoogleなどのクローラーに対して「このページはクロールしないで」と指示するファイルです。llms.txtはLLMに対してサイトの構造や記事一覧を伝えるためのファイルです。目的と対象が異なりますが、どちらもサイトのルートに置きます。</p></div>
<div class="faq-item"><p class="faq-q">Q. llms.txtはすべてのAIに対応していますか？</p><p class="faq-a">2026年時点では対応状況はAIによって異なります。Anthropicはllms.txtを参照することが知られています。まだ業界標準ではありませんが、設置コストがほぼゼロなのでやっておいて損はありません。</p></div>
<div class="faq-item"><p class="faq-q">Q. llms.txtはどこに設置すればいいですか？</p><p class="faq-a">サイトのルートに「llms.txt」という名前で設置します。GitHub Pagesの場合はリポジトリのルートディレクトリに置くだけです。</p></div>
<div class="faq-item"><p class="faq-q">Q. llms.txtに書くべき内容は何ですか？</p><p class="faq-a">サイト名・サイトの概要・カテゴリ一覧・記事一覧（タイトルとURL）・運営者情報が基本です。記事一覧では各記事の説明文を1〜2文で添えるとLLMが内容を把握しやすくなります。</p></div>
<div class="faq-item"><p class="faq-q">Q. llms.txtの設置効果はどうやって確認しますか？</p><p class="faq-a">直接的な効果測定は難しいです。ChatGPTやClaudeに自分のブログのトピックについて質問したとき、自分のブログや紹介しているサービスが回答に含まれるかどうかを定期的に確認する方法が現実的です。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="llmo-article-writing.html">AIに答えてもらいやすい記事の書き方を調べた｜LLMOって何？</a></div>
<div class="related-item"><a href="faq-structured-data.html">記事にFAQ構造化データを入れると検索結果がどう変わるか調べた</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)
print("記事8: llms-txt-setup.html 生成完了")


# ============================================================
# 記事9: google-index-not-found.html
# ============================================================
articles['google-index-not-found'] = build(
    slug='google-index-not-found',
    title='Googleにインデックスされるまで｜サイトマップ送信からの記録',
    desc='新規ブログ記事がGoogleにインデックスされるまでにやったことをまとめました。「URLがGoogleに登録されていません」の対処法、サイトマップ送信、インデックス登録リクエストの手順と待ち時間の目安を記録しています。',
    keywords='Google インデックス されない,インデックス 登録 リクエスト,サイトマップ 送信,URL 登録されていません',
    og_desc='新規ブログのインデックス登録で詰まった「URLがGoogleに登録されていません」の対処法とサイトマップ送信の手順をまとめました。',
    month='3',
    faq_ld=[
        ('「URLがGoogleに登録されていません」と表示された場合はどうすればいいですか？', 'まだGoogleにクロールされていない状態です。Search Consoleのデータ取得ツール（URL検査）で「インデックス登録をリクエスト」ボタンを押してください。リクエスト後、数日〜2週間でクロールされることが多いです。'),
        ('サイトマップを送信するとインデックスが早くなりますか？', 'サイトマップを送信するとGoogleのクローラーがサイトの全URLを把握しやすくなり、インデックス登録が早まる効果があります。特に新規サイトや記事数が多いサイトでは効果的です。'),
        ('新規サイトがGoogleにインデックスされるまでどれくらいかかりますか？', '一般的に1〜4週間程度かかります。新規ドメインはGoogleからの信頼が低いため、インデックスが遅い傾向があります。サイトマップ送信とインデックス登録リクエストを行うことで早める効果があります。'),
        ('インデックスされてもすぐに検索結果に表示されますか？', 'インデックス登録とは「Googleのデータベースに記事が登録された状態」です。その後、検索クエリとの関連性や品質評価によって順位が決まります。インデックス直後は順位が不安定で、安定するまで数週間〜数ヶ月かかることがあります。'),
        ('Search ConsoleなしでGoogleにインデックスされますか？', '自然にクロールされればSearch Consoleを使わなくてもインデックスされます。ただしSearch Consoleなしでは状況の把握や促進ができないため、ブログ運営では必ず設置することをおすすめします。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>「URLがGoogleに登録されていません」への対処手順</li>
<li>サイトマップ（sitemap.xml）の送信方法</li>
<li>インデックス登録リクエストの手順と上限</li>
<li>インデックスされるまでの待ち時間の目安</li>
</ul>
</div>

<p>こんにちは、ツバサです。このブログを公開してからGoogleに記事が表示されるまで、予想以上に時間がかかりました。詰まった「URLがGoogleに登録されていません」の対処法と、やったことをまとめておきます。</p>

<h2>インデックスとは何か</h2>

<p>Googleは世界中のウェブページを「クロール」（巡回）して内容を解析し、データベースに登録します。このデータベースへの登録のことを「インデックス」と呼びます。インデックスされていないページは検索結果に表示されません。</p>

<h2>「URLがGoogleに登録されていません」への対処</h2>

<p>Search ConsoleのURL検査ツールで記事のURLを入力すると、「URLがGoogleに登録されていません」と表示されることがあります。これはまだGoogleのクローラーがページを訪問・記録していない状態です。</p>

<p>対処手順は次の通りです。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>Search ConsoleのURL検査ツールにURLを入力してEnter</li>
<li>「URLがGoogleに登録されていません」と表示される</li>
<li>「インデックス登録をリクエスト」をクリック</li>
<li>処理が完了すると「インデックス登録をリクエスト済み」に変わる</li>
</ol>

<div class="warn-box">
<p><strong>注意：</strong>インデックス登録リクエストには1日あたりの上限があります（目安：10〜20件程度）。上限に達した場合は翌日に残りをリクエストしてください。</p>
</div>

<h2>サイトマップを送信する</h2>

<p>インデックス登録リクエストの他に、サイトマップを送信することでGoogleに全URLを一度に伝えられます。</p>

<ol style="padding-left:20px;margin-bottom:18px;line-height:2">
<li>Search Consoleの左メニュー「サイトマップ」をクリック</li>
<li>「新しいサイトマップの追加」欄に「sitemap.xml」と入力</li>
<li>「送信」をクリック</li>
<li>「成功しました」と表示されれば完了</li>
</ol>

<p>サイトマップが正しく送信されると、GoogleのクローラーがURLを認識しやすくなります。サイトを作ったらまず最初にやるべき作業です。</p>

<h2>インデックスされるまでの目安</h2>

<table class="spec-table">
<tr><th>状況</th><th>インデックスまでの目安</th></tr>
<tr><td>サイトマップ送信済み・リクエスト済み</td><td>数日〜1週間</td></tr>
<tr><td>リクエストのみ（サイトマップなし）</td><td>1〜2週間</td></tr>
<tr><td>何もしない（自然クロール待ち）</td><td>2週間〜数ヶ月</td></tr>
</table>

<p>新規ドメインはGoogleからの信頼（ドメイン権威）が低いため、既存の有名サイトよりもインデックスが遅い傾向があります。このブログも最初の記事がインデックスされるまで約2週間かかりました。</p>

<h2>インデックスされても順位はすぐ安定しない</h2>

<p>インデックスとは「Googleのデータベースに登録された状態」であり、即座に検索結果の上位に表示されるわけではありません。インデックス直後は順位が不安定で、数週間〜数ヶ月かけて「新規サイトブースト」が落ち着いてから本来の順位に落ち着きます。</p>

<p>このブログも公開直後は表示回数が多かったものの、2〜3ヶ月後に急減した時期がありました。これは新規サイトに対するGoogleの評価が安定化した典型的な動きで、インデックスの問題ではなく順位の問題です。Search Consoleで表示回数が減った場合は、まずインデックス状況を確認してから原因を判断することをおすすめします。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. 「URLがGoogleに登録されていません」と表示された場合は？</p><p class="faq-a">まだGoogleにクロールされていない状態です。URL検査画面で「インデックス登録をリクエスト」ボタンを押してください。リクエスト後、数日〜2週間でクロールされることが多いです。</p></div>
<div class="faq-item"><p class="faq-q">Q. サイトマップを送信するとインデックスが早くなりますか？</p><p class="faq-a">サイトマップを送信するとGoogleのクローラーがサイトの全URLを把握しやすくなり、インデックス登録が早まる効果があります。特に新規サイトや記事数が多いサイトでは効果的です。</p></div>
<div class="faq-item"><p class="faq-q">Q. 新規サイトがGoogleにインデックスされるまでどれくらいかかりますか？</p><p class="faq-a">一般的に1〜4週間程度かかります。サイトマップ送信とインデックス登録リクエストを行うことで早める効果があります。</p></div>
<div class="faq-item"><p class="faq-q">Q. インデックスされてもすぐに検索結果に表示されますか？</p><p class="faq-a">インデックス登録はGoogleのデータベースへの登録を意味します。その後、検索クエリとの関連性や品質評価によって順位が決まります。インデックス直後は順位が不安定で、安定するまで数週間〜数ヶ月かかることがあります。</p></div>
<div class="faq-item"><p class="faq-q">Q. 表示回数が急に減ったのはインデックスが外れたのですか？</p><p class="faq-a">必ずしもインデックスが外れたわけではありません。URL検査ツールでインデックス状況を確認し、「URLはGoogleに登録されています」と表示されれば順位低下が原因です。インデックス脱落とタイトル・コンテンツの問題を区別して対処することが重要です。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="search-console-basics.html">サーチコンソールの見方を覚えた備忘録｜表示回数・CTR・掲載順位</a></div>
<div class="related-item"><a href="search-console-ctr.html">記事のタイトルを変えたらCTRが動いた話｜サーチコンソール実録</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
</div>
</div>"""
)
print("記事9: google-index-not-found.html 生成完了")

# ============================================================
# 記事10: faq-structured-data.html
# ============================================================
articles['faq-structured-data'] = build(
    slug='faq-structured-data',
    title='記事にFAQ構造化データを入れると検索結果がどう変わるか調べた',
    desc='FAQ構造化データ（JSON-LD）をブログ記事に設置した記録です。FAQPage schemaの書き方、設置手順、リッチリザルトへの影響、AIへの情報伝達（LLMO）効果について調べてまとめました。',
    keywords='FAQ 構造化データ JSON-LD,FAQPage schema,リッチリザルト 設置,構造化データ ブログ',
    og_desc='FAQ構造化データ（JSON-LD）の書き方・設置手順・リッチリザルトへの影響・LLMO効果について調べた備忘録です。',
    month='3',
    faq_ld=[
        ('FAQ構造化データとは何ですか？', 'FAQ構造化データはページのよくある質問と回答を機械が読みやすい形式（JSON-LD）で記述したコードです。Googleはこのデータを認識して、検索結果にFAQのリッチリザルト（展開できる質問と回答のボックス）を表示することがあります。'),
        ('FAQのリッチリザルトは必ず表示されますか？', '必ずしも表示されるわけではありません。Googleは構造化データの内容、ページの品質、検索クエリとの関連性を総合的に判断してリッチリザルトを表示するかどうかを決めます。設置したからといって必ず表示されるわけではないですが、表示の機会が増えることは確かです。'),
        ('JSON-LDとはどういう意味ですか？', 'JSON-LD（JavaScript Object Notation for Linked Data）はデータを構造化して記述するための形式です。HTMLの中に&lt;script type="application/ld+json"&gt;タグで埋め込みます。Googleが推奨する構造化データの記述方式です。'),
        ('FAQ構造化データはすべての記事に入れるべきですか？', 'FAQがある記事には入れる価値があります。特にハウツー記事・比較記事・解説記事はFAQと相性が良いです。ただし、FAQの内容が薄い（一般的な質問だけ、答えが短すぎるなど）と効果が低くなります。実際の疑問に答える内容のFAQを5問以上用意するのが目安です。'),
        ('構造化データのエラーはどこで確認できますか？', 'Google Search Consoleの「拡張」セクションまたはGoogleのリッチリザルトテストツール（search.google.com/test/rich-results）で確認できます。エラーがある場合は該当箇所のJSONの記述を修正してください。'),
    ],
    body="""<div class="point-box">
<p><strong>この記事でわかること</strong></p>
<ul>
<li>FAQ構造化データ（JSON-LD）とは何か</li>
<li>FAQPage schemaの書き方と設置手順</li>
<li>リッチリザルト表示とSearch Consoleでの確認方法</li>
<li>AIへの情報伝達（LLMO）としての効果</li>
</ul>
</div>

<p>こんにちは、ツバサです。ブログのSEO対策を調べていて「構造化データ」という概念を知りました。設置すると検索結果にFAQが展開表示されることがあるというので、全記事に設置した記録をまとめておきます。</p>

<h2>FAQ構造化データとは</h2>

<p>FAQ構造化データはページの「よくある質問（FAQ）」と「回答」を、Googleが解析しやすい形式で記述したコードです。JSON-LD形式で書き、HTMLの&lt;head&gt;内または&lt;body&gt;末尾に埋め込みます。</p>

<p>Googleがこのデータを認識すると、検索結果にFAQの「リッチリザルト」が表示されることがあります。リッチリザルトとは、通常のタイトル・URLだけでなく、Q&Aが展開表示される形式です。</p>

<h2>FAQPage schemaの書き方</h2>

<p>FAQPage schemaの基本的な書き方は次の通りです。</p>

<div class="point-box">
<pre style="white-space:pre-wrap;font-size:13px;line-height:1.7">&lt;script type="application/ld+json"&gt;
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "質問文をここに書く",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "回答文をここに書く"
      }
    }
  ]
}
&lt;/script&gt;</pre>
</div>

<p>質問と回答のセットを複数追加する場合は、mainEntityの配列にオブジェクトを追加します。FAQの数は最低5問程度が目安です。</p>

<h2>設置手順と確認方法</h2>

<p>FAQPage schemaのコードをHTMLの&lt;head&gt;内か&lt;/body&gt;タグの直前に貼り付けます。GitHub Pagesでは各HTMLファイルに直接書き込む形で対応しました。</p>

<p>設置後、Googleの<a href="https://search.google.com/test/rich-results" target="_blank" rel="noopener noreferrer">リッチリザルトテスト</a>にURLを入力すると、構造化データが正しく認識されているかどうかを確認できます。「FAQPage」が検出された場合は設置成功です。</p>

<h2>実際に検索結果に反映されるまで</h2>

<p>構造化データを設置してからGoogleのリッチリザルトが表示されるまで、数週間〜1ヶ月程度かかることが一般的です。また設置しても必ずリッチリザルトが表示されるわけではなく、ページの品質や検索クエリとの関連性によってGoogleが表示の可否を判断します。</p>

<p>Search Consoleの「拡張」セクションに「FAQリッチリザルト」が表示されるようになったら、Googleが構造化データを認識してリッチリザルトの対象として評価している状態です。</p>

<h2>SEOだけでなくLLMOにも効果あり</h2>

<p>FAQ構造化データはGoogle検索（SEO）への効果だけでなく、ChatGPTやClaudeなどのAI（LLMO）への情報伝達にも効果があると言われています。LLMはFAQ形式のQ&A構造を引用しやすいため、構造化データで明示的に質問と回答を示すことで、AIが記事を参照する際に正確な情報が伝わりやすくなります。</p>

<p>特にサービス比較や「〇〇とは何か」という解説記事のFAQには、サービス名・具体的な数値・比較内容を含めると、AIが回答を生成する際に参照されやすくなります。</p>

<h2>よくある質問</h2>
<div class="faq-item"><p class="faq-q">Q. FAQ構造化データとは何ですか？</p><p class="faq-a">ページのよくある質問と回答を機械が読みやすい形式（JSON-LD）で記述したコードです。Googleはこのデータを認識して、検索結果にFAQのリッチリザルトを表示することがあります。</p></div>
<div class="faq-item"><p class="faq-q">Q. FAQのリッチリザルトは必ず表示されますか？</p><p class="faq-a">必ずしも表示されるわけではありません。Googleは構造化データの内容・ページの品質・検索クエリとの関連性を総合的に判断します。設置しておくことでリッチリザルト表示の機会が増えます。</p></div>
<div class="faq-item"><p class="faq-q">Q. FAQ構造化データはすべての記事に入れるべきですか？</p><p class="faq-a">FAQがある記事には入れる価値があります。実際の疑問に答える内容のFAQを5問以上用意するのが目安です。内容が薄いFAQは効果が低くなります。</p></div>
<div class="faq-item"><p class="faq-q">Q. 構造化データのエラーはどこで確認できますか？</p><p class="faq-a">GoogleのリッチリザルトテストツールかSearch Consoleの「拡張」セクションで確認できます。エラーがある場合は該当箇所のJSONを修正してください。</p></div>
<div class="faq-item"><p class="faq-q">Q. FAQ構造化データはAI（ChatGPT・Claude等）にも効果がありますか？</p><p class="faq-a">LLMはFAQ形式のQ&A構造を引用しやすいとされています。構造化データでQ&Aを明示することで、AIが記事を参照する際に正確な情報が伝わりやすくなります。SEOとLLMO両方への効果が期待できます。</p></div>""",
    related="""<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<div class="related-item"><a href="llmo-article-writing.html">AIに答えてもらいやすい記事の書き方を調べた｜LLMOって何？</a></div>
<div class="related-item"><a href="blog-seo-basics.html">個人ブログを始めてSEOを勉強した記録｜最初にやること5つ</a></div>
<div class="related-item"><a href="llms-txt-setup.html">llms.txtとは何か｜AIにブログを読ませるためのファイルを設置した</a></div>
</div>
</div>"""
)
print("記事10: faq-structured-data.html 生成完了")

# ============================================================
# 全記事をファイルに書き出す
# ============================================================
for slug, html in articles.items():
    path = f"{OUT}/{slug}.html"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"\n✅ 全{len(articles)}本のHTMLファイルを {OUT}/ に出力しました")

