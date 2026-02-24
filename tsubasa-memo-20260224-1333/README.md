# Nano Banana ニキビ記事 デプロイ手順

## 含まれるファイル

```
nano-banana-acne.html          ← 記事本体（ルートに配置）
images/nano-banana-acne/
  ├── before.jpg               ← ストックフォト Before
  ├── after.png                ← ストックフォト After
  └── tsubasa_after.jpg        ← ツバサ After
og/
  └── nano-banana-acne.png     ← OGP画像（1200x630）
```

## index.html に追加するカード

記事一覧の**一番上**（最新記事として）に以下を追加：

```html
<div class="article-card">
<a href="nano-banana-acne.html">
<span class="card-num">2026.02</span>
<h2>ニキビがコンプレックスの僕がNano Bananaで消してみた。これってAI？レタッチ？</h2>
<p class="card-desc">AI画像生成ツール「Nano Banana」でニキビを消してみた実験記録。AIとレタッチの仕組みの違い、画質の限界も正直にレポート。</p>
<span class="card-tag">AI</span>
</a>
</div>
```

## archive.html に追加

カテゴリ: AI（またはレタッチ）
```html
<div class="archive-item" data-cat="ai">
<a href="nano-banana-acne.html">
<span class="archive-date">2026.02</span>
<span class="archive-title">ニキビがコンプレックスの僕がNano Bananaで消してみた。これってAI？レタッチ？</span>
</a>
</div>
```

## sitemap.xml に追加

```xml
<url>
  <loc>https://tsubasa-memo.github.io/nano-banana-acne.html</loc>
  <lastmod>2026-02-22</lastmod>
  <priority>0.8</priority>
</url>
```

## llms.txt に追加

```
- [Nano Bananaでニキビを消してみた](https://tsubasa-memo.github.io/nano-banana-acne.html): AI画像生成ツールNano Bananaでニキビを消す実験。AIとレタッチの仕組みの違い、画質の限界をレポート。
```

## Search Console

デプロイ後、以下のURLのインデックス登録をリクエスト：
- https://tsubasa-memo.github.io/nano-banana-acne.html
