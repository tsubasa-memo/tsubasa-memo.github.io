# CLAUDE.md — ツバサのメモ帳 運用ガイド

このファイルはClaude Codeがリポジトリ内で作業する際のルールブックです。

## サイト概要

- **サイト名**: ツバサのメモ帳
- **URL**: https://tsubasa-memo.github.io/
- **ホスティング**: GitHub Pages（静的HTML）
- **コンセプト**: EC担当者「ツバサ」の備忘録ブログ（カメラ・写真・レタッチ・EC実務）
- **GA4**: G-YYBFXHXMM6

---

## ディレクトリ構成

```
/
├── index.html              ← トップページ（最新8件表示）
├── archive.html            ← 記事一覧（全件＋カテゴリフィルター）
├── 404.html                ← カスタム404ページ
├── [slug].html             ← 各記事（ケバブケース英語ファイル名）
├── thumbs/                 ← サムネイルSVG（320×180）
│   └── [slug].svg
├── og/                     ← OGP用PNG（1200×630）
│   ├── site.png            ← トップページ用
│   └── [slug].png          ← 各記事用
├── icons/
│   └── tsubasa.png         ← 著者アイコン
├── favicon.ico
├── favicon-16x16.png
├── favicon-32x32.png
├── sitemap.xml
├── robots.txt
├── llms.txt
└── CLAUDE.md               ← このファイル
```

---

## 記事追加の手順

新記事を追加するときは、以下の**5ステップ**を必ず実行する。

### 1. 記事HTML作成

ファイル名: `[slug].html`（英語ケバブケース）

既存記事（例: `exif-info.html`）のHTML構造をそのまま踏襲する。以下のテンプレート構造を守ること。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YYBFXHXMM6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-YYBFXHXMM6');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[記事タイトル]｜ツバサのメモ帳</title>
<meta name="description" content="[120文字程度の要約]">
<meta name="keywords" content="[カンマ区切りキーワード]">
<meta property="og:title" content="[記事タイトル]｜ツバサのメモ帳">
<meta property="og:description" content="[OG用の短い説明]">
<meta property="og:type" content="article">
<meta property="og:locale" content="ja_JP">
<meta property="og:url" content="https://tsubasa-memo.github.io/[slug].html">
<meta property="og:image" content="https://tsubasa-memo.github.io/og/[slug].png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://tsubasa-memo.github.io/og/[slug].png">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://tsubasa-memo.github.io/[slug].html">
<!-- JSON-LD: FAQPage -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[質問]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[回答]"
      }
    }
  ]
}
</script>
<!-- CSS: 既存記事からコピー。サイト共通のCSS変数を使用 -->
<style>
/* 既存記事と同一のCSSを使う。個別記事で独自CSSを追加しない */
</style>
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
</head>
<body>
<!-- ヘッダー -->
<header>
<div class="wrap">
<a href="index.html" class="site-name">ツバサのメモ帳</a>
<span class="site-tag">備忘録ブログ</span>
</div>
</header>

<!-- パンくず -->
<nav class="breadcrumb">
<div class="wrap">
<a href="index.html">ホーム</a> ＞ [記事の短縮タイトル]
</div>
</nav>

<!-- ヒーロー -->
<div class="hero">
<div class="wrap">
<h1>[記事タイトル（改行位置は内容に応じて調整）]</h1>
<p class="update">[YYYY]年[M]月 更新</p>
</div>
</div>

<!-- 本文 -->
<main>
<div class="wrap">
<!-- 導入文: 「こんにちは、ツバサです。」から始める -->
<!-- 本文セクション: h2 / h3 / h4 で構造化 -->
<!-- 表: <table>タグ使用 -->
<!-- FAQ: 「よくある質問」セクション（h2） -->

<!-- 著者プロフィール（末尾） -->
<div class="author-box">
<div class="author-icon"><img src="icons/tsubasa.png" alt="ツバサ" width="64" height="64"></div>
<div class="author-text">
<p class="author-name">ツバサ</p>
<p>EC関係の仕事をしています。このサイトは自分が調べたことの備忘録です。Photoshopは少し使えますが苦手で、ちょっとした画像補正はもっぱらスマホアプリ派。アプリで対応しきれない本格的なレタッチはプロに依頼しています。</p>
</div>
</div>

<!-- 関連記事 -->
<div class="related">
<h2 class="related-title">関連する記事</h2>
<div class="related-list">
<!-- 同カテゴリから2〜3件 -->
</div>
</div>

</div>
</main>

<footer>
<div class="wrap">&copy; 2026 ツバサのメモ帳</div>
</footer>
</body>
</html>
```

### 2. サムネイルSVG作成

- パス: `thumbs/[slug].svg`
- サイズ: `viewBox="0 0 320 180"`（16:9）
- デザインルール:
  - 背景: `linearGradient` で2色のグラデーション（既存サムネを参照してカテゴリに合った色を選ぶ）
  - 角丸: `rx="4"`
  - メインテキスト: `font-size="13"`, `font-weight="600"`, 白（`rgba(255,255,255,.95)`）
  - サブテキスト: `font-size="11"`, 白（`rgba(255,255,255,.6)`）
  - テキスト位置: `text-anchor="middle"`, x="160"（中央揃え）
  - イラスト要素: 記事テーマに合った簡易アイコンを`rect`, `circle`, `path`で描画
  - フォント: `font-family="sans-serif"`
- 既存のSVGをカテゴリ別に参照:
  - カメラ系: `first-camera.svg`（青系 #2e6b8a → #1a4a62）
  - レタッチ系: `retouch-services.svg`（ティール系）
  - AI系: `nano-banana-acne.svg`（紫系）
  - 写真・撮影系: `id-photo.svg`（オレンジ系 #dc7a28 → #a16207）
  - EC・実務系: `ec-image-rules.svg`（緑系）
  - 副業・キャリア系: `video-vs-retouch-career.svg`（紫系 #7c3aed → #4c1d95）

### 3. OGP画像生成

- パス: `og/[slug].png`
- サイズ: 1200×630px
- 生成方法: サムネイルSVGをcairosvgで拡大変換

```bash
python3 -c "
import cairosvg
cairosvg.svg2png(
    url='thumbs/[slug].svg',
    write_to='og/[slug].png',
    output_width=1200,
    output_height=630
)
"
```

※ cairosvgがインストールされていない場合: `pip install cairosvg --break-system-packages`

### 4. index.html の更新

- **新記事を記事リストの先頭に追加**する
- 新記事には `<span class="card-num new">NEW</span>` を付ける
- **直前まで`NEW`だった記事のcard-numを日付に変更**する（例: `<span class="card-num">2026.03</span>`）
- 記事リストは**最新8件**を表示する（9件以上になったら古い記事をリストから外す。archive.htmlには残す）
- 「すべての記事を見る」ボタンの件数を更新する

記事カードのHTML構造（サムネあり版）:

```html
<div class="article-card">
<a href="[slug].html">
<div class="card-thumb"><img src="thumbs/[slug].svg" alt="[alt文]" width="320" height="180"></div>
<div class="card-body">
<span class="card-num new">NEW</span>
<h2>[記事タイトル]</h2>
<p class="card-desc">[1〜2行の概要]</p>
<span class="card-tag">[カテゴリ名]</span>
</div>
</a>
</div>
```

### 5. archive.html の更新

- 新記事を該当カテゴリの先頭に追加する
- 記事カードの構造はindex.htmlと同じ
- `data-cat` 属性でカテゴリを指定する（JavaScriptフィルター用）
- カテゴリ値: `camera`, `retouch`, `ai`, `photo`, `ec`, `career`

---

## カテゴリ一覧

| カテゴリ名 | data-cat値 | 表示名 |
|---|---|---|
| カメラ | camera | カメラ |
| レタッチ | retouch | レタッチ |
| AI | ai | AI |
| 写真・撮影 | photo | 写真・撮影 |
| EC・実務 | ec | EC・実務 |
| 副業・キャリア | career | 副業・キャリア |

---

## sitemap.xml / llms.txt の更新

新記事追加時は以下も更新する。

### sitemap.xml
```xml
<url>
  <loc>https://tsubasa-memo.github.io/[slug].html</loc>
  <lastmod>[YYYY-MM-DD]</lastmod>
  <changefreq>monthly</changefreq>
</url>
```

### llms.txt
該当カテゴリのセクションに記事情報を追加。

---

## Git コミットルール

- コミットメッセージは日本語
- 形式: `add: [記事の短縮タイトル]` または `update: [変更内容]`
- 例:
  - `add: ミラーレスカメラ選び方記事`
  - `update: index.html 記事順序変更`
  - `fix: exif-info.html typo修正`

---

## 絶対に守ること

### プロフィール文は固定
以下のプロフィール文を勝手に変更しない。全記事で統一。

> EC関係の仕事をしています。このサイトは自分が調べたことの備忘録です。Photoshopは少し使えますが苦手で、ちょっとした画像補正はもっぱらスマホアプリ派。アプリで対応しきれない本格的なレタッチはプロに依頼しています。

### CSS変数
全ページ共通。個別記事で独自の色やフォントを追加しない。

```css
:root {
  --bg: #f8f7f4;
  --text: #2d2d2d;
  --text-sub: #666;
  --accent: #2e6b8a;
  --accent-light: #e8f0f5;
  --border: #e0ddd8;
  --card: #fff;
  --link: #2e6b8a;
  --tag-bg: #f2f0ec;
}
```

### 記事の文体
- 一人称: 「僕」
- 口調: 丁寧だがかしこまりすぎない。友人に説明するような距離感
- 冒頭: 「こんにちは、ツバサです。」で始める
- 外部リンク: `rel="noopener noreferrer nofollow"` を付ける
- 製品リスト前の注記: 「※ 機種名をクリックするとメーカー公式の製品ページに移動します。」等

### ファイル命名規則
- 記事HTML: 英語ケバブケース（`nano-banana-acne.html`）
- サムネSVG: 記事HTMLと同名（`thumbs/nano-banana-acne.svg`）
- OG画像: 記事HTMLと同名（`og/nano-banana-acne.png`）

---

## 既存記事一覧（参照用）

| ファイル名 | タイトル | カテゴリ |
|---|---|---|
| nano-banana-acne.html | Nano Bananaでニキビを消してみた | AI |
| coworking-spaces-tokyo.html | コワーキングスペース都内7選 | 副業・キャリア |
| retouch-services.html | レタッチ外注サービス7社比較 | レタッチ |
| video-vs-retouch-career.html | 動画編集 vs レタッチャー | 副業・キャリア |
| id-photo.html | スマホで証明写真を作る方法 | 写真・撮影 |
| exif-info.html | Exif情報と位置情報の削除方法 | 写真・撮影 |
| ec-image-rules.html | ECサイト商品画像ルールまとめ | EC・実務 |
| background-white.html | 背景白抜きの方法まとめ | レタッチ |
| first-camera.html | 初めてのカメラ選び | カメラ |
| camera-smartphones.html | カメラ性能で選ぶスマホ | カメラ |
| sd-card.html | SDカードの選び方 | カメラ |
| retouch-apps.html | スマホレタッチアプリ5選 | レタッチ |
| what-is-retouch.html | レタッチとは？ | レタッチ |

---

## よく使うコマンド例

### 記事追加（全ステップ一括）
```bash
# 1. 記事HTML作成 → [slug].html
# 2. サムネSVG作成 → thumbs/[slug].svg
# 3. OGP画像生成
python3 -c "import cairosvg; cairosvg.svg2png(url='thumbs/[slug].svg', write_to='og/[slug].png', output_width=1200, output_height=630)"
# 4. index.html 更新（先頭に追加、旧NEWを日付に）
# 5. archive.html 更新
# 6. sitemap.xml 更新
# 7. llms.txt 更新
# 8. コミット＆プッシュ
git add .
git commit -m "add: [記事タイトル短縮版]"
git push origin main
```
