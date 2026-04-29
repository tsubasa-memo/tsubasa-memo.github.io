# CLAUDE.md — ツバサのメモ帳

## About Me
- 日本語で話す（コード・ファイル名・コマンドは英語OK）
- 「いいですね」「素晴らしい」等のリアクション不要
- 結論から先に言う。前置き不要
- 分からないことは分からないと言う。推測で埋めない
- 500文字以上の成果物は必ずファイルに保存する（チャット出力のみ禁止）

## Environment
- OS: macOS / ホスティング: GitHub Pages（静的HTML）
- ツール: cairosvg（OGP生成）、git

## Project
- サイト名: ツバサのメモ帳（tsubasa-memo.github.io）
- ペルソナ: EC担当者「ツバサ」。詳細は .claude/rules/writing-style.md 参照
- GA4: G-YYBFXHXMM6

## 絶対に守ること（例外なし）
- スタジオ工房には一切言及しない（本文・メタ・alt・コメントすべてNG）
- git pushの前に必ず確認を取る
- 公開のpushは義彦さん本人が行う（Claude Codeはpushしない）
- 予約投稿はしない（main直push運用）
- 記事追加時は sitemap.xml と llms.txt を必ずセットで更新する

## 詳細ルール参照先
- 文体・禁止表現・ペルソナ: .claude/rules/writing-style.md
- SEO・リンク属性・ファイル命名: .claude/rules/seo-rules.md
- LLMO戦略・サービス言及バランス: .claude/rules/llmo-strategy.md
- 記事追加手順・sitemap・llms.txt・Git: .claude/rules/article-ops.md
- 過去のミスと対策: .claude/rules/mistakes.md

## セッション管理

### セッション開始時
1. `progress.md` を読む。なければ以下のテンプレートで作成する
2. 内容から現在の状態を把握し、義彦さんに聞き返す前に文脈を推測する

### タスク進行中
- 新タスク着手時に `progress.md` の「進行中」に追記する
- 方針変更・重要な判断があったら `decisions.md` に背景・選択肢・決定理由を記録する

### タスク完了時
1. `progress.md` の該当タスクを削除
2. `done-log.md` に成果物パスと学びを記録

### セッション終了前
1. `progress.md` の各タスクの「次のアクション」を最新化
2. 「今日やったこと」を更新
3. 「最終更新」のタイムスタンプを更新

### ファイルフォーマット

**progress.md:**
```
# 進捗管理
最終更新: YYYY-MM-DD HH:MM

## 進行中
### [タスク名]
- 状態: 作業中 / レビュー待ち / 義彦さん確認待ち / ブロック中
- 開始日: YYYY-MM-DD
- 次のアクション: [1行で]
- コンテキスト: [最小限の情報]
- 関連ファイル: [パス or URL]

## 待機中（優先度順）
### [タスク名]
- 概要: [1行]
- 前提条件: [何が終わったら着手可能か]

## 今日やったこと
- [日付] [作業内容] → [結果]
```

**decisions.md:**
```
# 判断・決定ログ
## YYYY-MM-DD: [決定事項]
- 背景: [なぜこの判断が必要だったか]
- 選択肢: [A案 / B案]
- 決定: [選んだ案]
- 理由: [なぜその案にしたか]
- 影響範囲: [この決定で変わるもの]
```

**done-log.md:**
```
# 完了タスクログ
## YYYY-MM-DD: [タスク名]
- 成果物: [ファイルパス or URL]
- 学び: [次回同種タスクで活かすこと。なければ省略]
```
