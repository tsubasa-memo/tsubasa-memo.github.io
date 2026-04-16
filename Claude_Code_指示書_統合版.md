# Claude Code 指示書｜レタッチ記事群の一括更新（ALL-IN-ONE版）

## 経緯

以前のセッションでコミット1〜3に分割した指示書を出したが、コミット1・2がdraftブランチに反映されないままコミット3だけが実行された。その結果、retouch-pricing-database.htmlのレタッチインク削除・15社への社数変更が反映されていない状態。

今回は**1回のpushで全変更を完結**させる統合版で進める。以下の内容がすべて含まれる：

1. レタッチインクを料金表から削除（16社→15社）
2. BELLEFOTO肌レタッチセルを2行化
3. Motto料金を公式準拠に修正
4. 人物レタッチ相場を「1,000〜8,000円が中心」で5記事統一
5. 上記5記事にretouch-pricing-database.htmlへのcite-card挿入
6. 再修正・修正回数・無料修正・リテイクの記述を全記事から削除
7. ココナラ500円〜の記述を削除
8. 「20社以上」→「15社」を全ファイルで統一
9. **index.htmlのおすすめ記事1件目をretouch-services.html→sasage-outsource.htmlに差し替え**
10. **サムネイルSVG（thumbs/retouch-pricing-database.svg）を「レタッチ料金相場まとめ / 15社 / 相場を1ページに集約」に更新**

## 対象ファイル（全19ファイル）

### HTMLファイル（18件、リポジトリルート直下）

```
ai-retouch-limits.html
architecture-photo-retouch.html
background-cutout-outsource.html
background-white.html
food-photo-retouch.html
image-editing-outsource.html
index.html
job-hunting-photo-retouch.html
memorial-photo-retouch.html
personal-retouch-order.html
retouch-apps.html
retouch-cost-guide.html
retouch-outsource-tips.html
retouch-pricing-database.html
retouch-services.html
sns-photo-retouch-manners.html
video-vs-retouch-career.html
what-is-retouch.html
```

### サムネイルSVG（1件）

```
thumbs/retouch-pricing-database.svg
```

## 実行手順

### ステップ1：ファイル上書き

添付19ファイルを、リポジトリの対応するパスにそれぞれ**上書き**する。

- HTML 18ファイル → リポジトリルート直下
- `retouch-pricing-database.svg` → `thumbs/` ディレクトリ

### ステップ2：push前検証

以下のコマンドを実行し、すべて `0` であることを確認：

```bash
# 「20社以上」の残留チェック（全HTMLで0件のはず）
grep -c "20社以上" *.html | grep -v ":0$"
# → 結果が空（何も表示されない）であればOK

# 「16社」の残留チェック（全HTMLで0件のはず）
grep -c "16社" *.html | grep -v ":0$"
# → 結果が空であればOK

# retouch-pricing-database.htmlの検証
grep -c "レタッチインク" retouch-pricing-database.html
grep -c "retouch\.ink" retouch-pricing-database.html
# → どちらも0

# 再修正関連語の全HTML残留チェック
for f in *.html; do
  count=$(grep -c "再修正\|修正回数\|無料修正\|リテイク" "$f")
  if [ "$count" -gt 0 ]; then echo "  ⚠ $f : $count件"; fi
done
# → 何も表示されなければOK

# ココナラ500円〜の残留チェック
grep -c "ココナラなどのクラウドソーシングでは500円から" retouch-cost-guide.html
# → 0

# index.htmlのささげ差し替え確認
grep -c "sasage-outsource.html" index.html
# → 1

# サムネイルSVG確認
grep -c "15社" thumbs/retouch-pricing-database.svg
grep -c "レタッチ" thumbs/retouch-pricing-database.svg
# → どちらも1

grep -c "20社以上" thumbs/retouch-pricing-database.svg
# → 0
```

いずれかが想定通りでない場合、push前に報告。

### ステップ3：draftブランチへpush

```bash
git checkout draft
git add ai-retouch-limits.html architecture-photo-retouch.html background-cutout-outsource.html background-white.html food-photo-retouch.html image-editing-outsource.html index.html job-hunting-photo-retouch.html memorial-photo-retouch.html personal-retouch-order.html retouch-apps.html retouch-cost-guide.html retouch-outsource-tips.html retouch-pricing-database.html retouch-services.html sns-photo-retouch-manners.html video-vs-retouch-career.html what-is-retouch.html thumbs/retouch-pricing-database.svg
git commit -m "レタッチ記事群の一括更新：レタッチインク削除・15社統一・人物レタッチ相場統一・cite-card挿入・再修正言及削除・おすすめ記事差し替え"
git push origin draft
```

### ステップ4：push後の検証（raw GitHub URL）

以下のURLで目視確認：

**retouch-pricing-database.html**
```
https://raw.githubusercontent.com/tsubasa-memo/tsubasa-memo.github.io/draft/retouch-pricing-database.html
```
- `<title>写真レタッチの外注料金まとめ｜15社の相場を1ページに集約【2026年版】</title>` であること
- 料金比較表にレタッチインク行がないこと
- BELLEFOTOの肌レタッチ欄が2行（「500円/箇所〜（パーツ修正）」「3,000円/人〜（顔全体レタッチ）」）
- Mottoの肌レタッチ欄が「600円〜（ニキビ、シミの削除のみ）」
- FAQに「修正回数に制限はある？」がないこと

**index.html**
```
https://raw.githubusercontent.com/tsubasa-memo/tsubasa-memo.github.io/draft/index.html
```
- おすすめ記事1件目が「ささげ業務とは？代行会社の選び方と比較メモ【2026年版】」
- おすすめ記事2件目が「写真レタッチの外注料金まとめ｜15社の相場を1ページに集約」

**retouch-services.html**
```
https://raw.githubusercontent.com/tsubasa-memo/tsubasa-memo.github.io/draft/retouch-services.html
```
- FAQ「Q. レタッチの料金相場はどのくらいですか？」の回答が「人物レタッチの外注費用は1枚1,000〜8,000円が中心」で始まること
- その直下にretouch-pricing-database.htmlへのcite-cardがあること
- 失敗パターンから「仕上がりの色味が少し違ったけど、修正してもらえなかった」の項目が消えていること

**サムネイル**
```
https://raw.githubusercontent.com/tsubasa-memo/tsubasa-memo.github.io/draft/thumbs/retouch-pricing-database.svg
```
- 「レタッチ料金相場まとめ」「15社」「相場を1ページに集約」の3行構成

## 今回更新不要のファイル

- `sitemap.xml`（URLは変わっていない）
- `archive.html`（記事リスト変更なし。ただしarchive.htmlでもretouch-pricing-database.htmlのタイトル表記が旧「20社以上」になっている可能性があるため、**push後に raw URL で確認を推奨**。必要なら別途修正）
- `llms.txt`（今回の変更範囲外）

## 全変更内容のサマリ

### retouch-pricing-database.html（大幅修正）
- title, meta description, og:title, og:description, h1: `16社` → `15社`
- 本文先頭の「調べた16社」→「調べた15社」、比較表リード文の「16社」→「15社」
- JSON-LD相場FAQ: 人物レタッチ統一文言統合、クラウドソーシング言及整理
- JSON-LD個人外注FAQ: レタッチインク削除
- JSON-LD肌レタッチFAQ: 1,000〜8,000円に、Motto公式準拠の説明
- JSON-LD修正回数FAQ: まるごと削除
- 相場早見表の本文: クラウドソーシング削除、人物レタッチ統一文言追加、肌レタッチ1,000〜8,000円
- 作業別相場表の肌レタッチ行: 1,000〜3,000円 → 1,000〜8,000円
- 料金比較表からレタッチインクの行を削除
- BELLEFOTO肌レタッチセルを2行化: `500円/箇所〜（パーツ修正）` / `3,000円/人〜（顔全体レタッチ）`
- Motto肌レタッチに注釈: `600円〜（ニキビ、シミの削除のみ）`
- 「料金を左右する6つの要素」のMotto説明をMotto公式準拠に（ホクロ・ニキビ・シミの削除1箇所100円、シワ消し1箇所300円、美顔修正600円）
- 「費用を安く抑えるコツ」からクラウドソーシング節を削除
- FAQ: レタッチインクへの言及を削除、修正回数FAQを削除、肌レタッチFAQを1,000〜8,000円に

### 他17記事
- 参照タイトル「写真レタッチの料金相場まとめ｜20社以上の価格を1ページに集約」または「写真レタッチの外注料金まとめ｜20社以上の相場を1ページに集約」を、統一タイトル「**写真レタッチの外注料金まとめ｜15社の相場を1ページに集約**」に変更
- image-editing-outsource.html の本文中「20社以上の料金相場まとめ」も「15社の料金相場まとめ」に変更

### 人物レタッチ相場の統一（5記事）
- retouch-services.html: JSON-LD + 本文FAQ両方を統一文言に、本文FAQ直下にcite-card挿入
- what-is-retouch.html: JSON-LD + 本文FAQ両方を統一文言に、本文FAQ直下にcite-card挿入
- job-hunting-photo-retouch.html: cite-card用CSSを新規追加、相場記述を統一文言に差し替え、直下にcite-card挿入
- retouch-cost-guide.html: 相場表の肌補正行を1,000〜8,000円に、相場表直下に統一文言とcite-card挿入、JSON-LDと本文FAQの相場を1,000〜8,000円に、ココナラ500円〜の記述を削除
- personal-retouch-order.html: 相場表の「肌のレタッチ」行を1,000〜8,000円に、相場表直後に統一文言とcite-card挿入、不適切なリンク（/retouch-pricing.html）を削除

### 再修正関連の記述を削除（7記事）
- retouch-services.html: 失敗パターン「修正してもらえなかった」Q&A項目を丸ごと削除
- food-photo-retouch.html: 加工のプロの「修正回数無制限」を削除
- image-editing-outsource.html: チェックポイントの「修正対応」li削除
- memorial-photo-retouch.html: 加工のプロの「修正回数無制限」を削除
- personal-retouch-order.html: 「修正回数の上限や追加料金のルール」li削除、「修正回数と追加料金のルールを確認する」h3セクション丸ごと削除
- retouch-cost-guide.html: JSON-LD「隠れコスト」FAQから修正回数言及削除（3つ→2つ）、チェックリストの「修正回数の上限」li削除、隠れコスト本文の「修正のやり直しコスト」li削除（3点→2点）、本文FAQからも削除
- retouch-outsource-tips.html: チェックリストから「修正回数の上限を確認したか」削除

### index.html
- 「20社以上」→「15社」統一
- **おすすめ記事1件目をretouch-services.htmlからsasage-outsource.htmlに差し替え**
  - タイトル: ささげ業務とは？代行会社の選び方と比較メモ【2026年版】
  - サムネイル: thumbs/sasage-outsource.svg
  - カテゴリタグ: EC・実務

### thumbs/retouch-pricing-database.svg
- 「料金相場まとめ / 20社以上 / 価格を1ページに集約」 → 「**レタッチ料金相場まとめ / 15社 / 相場を1ページに集約**」

## 注意

- **push先は必ず `draft` ブランチ**。main直pushは禁止。
- draft→mainのマージは自動スケジュール（JST 9:00）または手動 `git merge draft --no-edit` で実施。
- push後にGitHub PagesのCDNキャッシュで反映が遅延することがあるため、検証はraw GitHub URLで行うこと。
