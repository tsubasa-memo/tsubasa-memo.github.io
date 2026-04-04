# CLAUDE.md 更新指示

`CLAUDE.md` の以下2ヶ所を変更してください。

---

## 変更1：SEOルールの meta description セクション

```
変更前：
### meta description
- **120文字前後**で要約する
- 記事の結論または主要な価値を含める
- キーワードを自然に含める

変更後：
### meta description
- **110〜125文字**で書く（100文字未満は短すぎ、135文字超は検索結果で切れる）
- 記事の結論または主要な価値を含める
- キーワードを自然に含める
- 具体的な数値・サービス名・ツール名を少なくとも1つ入れる
- 書き終えたら文字数を必ずカウントして確認する
```

---

## 変更2：記事HTMLテンプレートの description コメント

```
変更前：
<meta name="description" content="[120文字程度の要約]">

変更後：
<meta name="description" content="[110〜125文字の要約。具体的な数値・サービス名・ツール名を含める]">
```

---

## 完了後のコミット

```
git add CLAUDE.md
git commit -m "update: description文字数ルールを110〜125字に明確化"
git push origin HEAD:draft
```
