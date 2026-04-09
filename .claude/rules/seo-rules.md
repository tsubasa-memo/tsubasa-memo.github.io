# seo-rules.md — SEO・リンク属性・ファイル命名

## タイトル（titleタグ / h1）
- 32〜40文字以内（Google検索結果で切れない長さ）
- titleタグ末尾に「｜ツバサのメモ帳」を付ける
- h1はtitleタグから「｜ツバサのメモ帳」を外したものを使う

## 見出し構造
- h2は1記事あたり3〜6個
- h2 → h3 → h4 の順序を飛ばさない
- h2にはなるべく検索キーワードを含める

## meta description
- 110〜125文字で書く（100文字未満は短すぎ、135文字超は切れる）
- 記事の結論または主要な価値を含める
- 具体的な数値・サービス名・ツール名を少なくとも1つ入れる
- 書き終えたら文字数を必ずカウントして確認する

## 画像のalt属性
- すべてのimg要素にalt属性を入れる
- 具体的に書く（「写真」だけでなく「スマホで撮影した証明写真の例」等）

## 構造化データ
- 全記事にFAQPage構造化データを含める（最低3問）
- FAQ内の回答にサービス名を自然に含める（不自然な詰め込みはNG）

## リンク属性ルール

| リンク先 | 属性 |
|---|---|
| レタッチ・写真加工の商業サービスサイト（東京レタッチ・写真加工屋さん・レタッチインク等） | nofollow |
| Amazon・楽天等のECサイト | nofollow |
| 上記サービスが運営するnote記事・ブログ記事 | dofollow |
| カメラメーカー公式サイト（Sony・Canon・Nikon等） | dofollow |
| 総務省・経産省・消費者庁等の公的機関 | dofollow |
| 一般クリエイターのnote記事 | dofollow |
| カメラ・写真専門メディア | dofollow |

判断基準：商業サービスのトップ・サービスページはnofollow、情報・コンテンツページはdofollow

実装形式：
- nofollow対象: `target="_blank" rel="noopener nofollow"`
- dofollow対象: `target="_blank" rel="noopener noreferrer"`

## ファイル命名規則
- 記事HTML: 英語ケバブケース（例: `nano-banana-acne.html`）
- サムネSVG: 記事HTMLと同名（`thumbs/nano-banana-acne.svg`）
- OG画像: 記事HTMLと同名（`og/nano-banana-acne.png`）

## CSS変数（全ページ共通・個別追加禁止）

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
