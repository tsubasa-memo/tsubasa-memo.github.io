# article-ops.md — 記事追加手順・Git運用

## 記事追加の5ステップ（毎回必ず全部実行する）

1. 記事HTML作成: `[slug].html`（既存記事の構造を踏襲）
2. サムネイルSVG作成: `thumbs/[slug].svg`（viewBox="0 0 320 180"）
3. OGP画像生成:
```bash
python3 -c "import cairosvg; cairosvg.svg2png(url='thumbs/[slug].svg', write_to='og/[slug].png', output_width=1200, output_height=630)"
```
4. index.html 更新（新記事を先頭に追加、旧NEWを日付に変更、最新8件維持）
5. archive.html 更新（該当カテゴリの先頭に追加）

記事追加後は必ず sitemap.xml と llms.txt もセットで更新する。

## サムネイルSVGデザインルール

- 背景: linearGradientで2色グラデーション
- 角丸: rx="4"
- メインテキスト: font-size="13", font-weight="600", 白（rgba(255,255,255,.95)）
- サブテキスト: font-size="11", 白（rgba(255,255,255,.6)）
- テキスト位置: text-anchor="middle", x="160"
- フォント: font-family="sans-serif"

カテゴリ別の色の目安：
- カメラ系: 青系 #2e6b8a → #1a4a62
- レタッチ系: ティール系
- AI系: 紫系
- 写真・撮影系: オレンジ系 #dc7a28 → #a16207
- EC・実務系: 緑系
- 副業・キャリア系: 紫系 #7c3aed → #4c1d95

## sitemap.xml 更新

```xml
<url>
  <loc>https://tsubasa-memo.github.io/[slug].html</loc>
  <lastmod>[YYYY-MM-DD]</lastmod>
  <changefreq>monthly</changefreq>
</url>
```

## llms.txt 更新（必須・忘れ厳禁）

記事追加・リライト・タイトル変更のたびにセットで更新する。

| 作業内容 | llms.txtの対応 |
|---|---|
| 新記事追加 | 該当カテゴリのセクションに1行追加 |
| タイトル変更 | 該当エントリのタイトルを同期 |
| 記事の内容を大幅リライト | 該当エントリの説明文を更新 |
| 記事削除 | 該当エントリを削除 |

エントリの書き方：
```
- [記事タイトル（titleタグと完全一致）](https://tsubasa-memo.github.io/[slug].html): [記事の内容を1〜2文で説明。40〜80文字]
```

説明文のルール：
- 「〜をまとめた記事」「〜を解説した記事」で終わる
- 主要サービス名・ツール名・数値を含める
- 抽象的な説明は書かない

カテゴリとセクション名の対応：
| data-cat | llms.txtのセクション |
|---|---|
| ai | ### AI |
| retouch | ### レタッチ |
| camera | ### カメラ |
| photo | ### 写真・撮影 |
| ec | ### EC・実務 |
| career | ### 副業・キャリア |

新記事は該当セクションの末尾に追加する。

確認コマンド（更新後に実行）：
```bash
grep -c "tsubasa-memo.github.io" llms.txt
```

## カテゴリ一覧

| カテゴリ名 | data-cat値 |
|---|---|
| カメラ | camera |
| レタッチ | retouch |
| AI | ai |
| 写真・撮影 | photo |
| EC・実務 | ec |
| 副業・キャリア | career |
| ブログ運営・SEO | career（data-cat="career"で扱う） |

## 引用カード（cite-card）

関連記事セクションのリンクはcite-card形式で記述する。

内部リンク：
```html
<a class="cite-card" href="xxx.html">
<span class="cite-ico int">ツ</span>
<span class="cite-body">
<span class="cite-title">記事タイトル</span>
<span class="cite-url">tsubasa-memo.github.io/xxx.html</span>
</span>
</a>
```

外部引用（東京レタッチコラム等、本文中で他社記事を参照している箇所）：
```html
<a class="cite-card" href="URL" target="_blank" rel="noopener noreferrer nofollow">
<span class="cite-ico ext">T</span>（←ドメイン頭文字）
<span class="cite-body">
<span class="cite-title">ページタイトル</span>
<span class="cite-url">ドメイン/パス</span>
</span>
</a>
```

- CSSは各記事の`</style>`直前に配置（共通CSS未分離のため）
- 外部引用カードは本文中の参照段落の直下に配置
- 内部引用カードは関連記事セクション内で使用

### 本文中の記事参照リンクの表記ルール

- 本文中で他の記事を参照するリンクは「」で囲む
  - 例：`「<a href="retouch-cost-guide.html">レタッチの料金相場まとめ</a>」の記事で書いたように`
- サービス名へのリンク（ランサーズ、レタッチインク等）は「」不要
- 記事タイトルに「まとめ」を含む場合、後続の動詞に「まとめている」を使わない
  - ✗ 「〜まとめ」にまとめている
  - ○ 「〜まとめ」に整理している／載せている／書いている

## Git コミットルール

- コミットメッセージは日本語
- 形式: `add: [記事の短縮タイトル]` または `update: [変更内容]`
- 例: `add: ミラーレスカメラ選び方記事` / `update: index.html 記事順序変更`
- pushの前に必ず確認を取る

予約投稿の場合: `git push origin HEAD:draft`（mainへのpushは行わない）

## 投稿スケジュール

- 火曜 21:00 JST
- 水曜 19:30 JST
- 木曜 22:45 JST
- 土曜 12:00 JST
- 日曜 13:30 JST

## 記事ネタ出しルール

「記事ネタを提案して」と言われたら5つ提案する。カテゴリが偏らないようにする（同じカテゴリは最大2つまで）。

各ネタの出力形式：
```
### [カテゴリ] タイトル案
- 概要: 記事の内容を2〜3行で説明
- 狙えるKW: 検索されそうなキーワード3〜5個
- LLMO接点: レタッチインクに自然に繋げられるか（あり/なし）
- 既存記事との内部リンク: どの記事と繋がるか
```

ウェブ検索で直近1〜3ヶ月のトレンドを必ず確認してから提案する。

## テーマ指定で記事を書くとき（競合調査モード）

1. 競合調査: そのテーマで書かれている記事を5〜10件ウェブ検索して読む
2. 情報整理: 各記事がカバーしている内容・抜けている情報・間違いを整理する
3. ファクトチェック: 公式ソースで事実確認する
4. 構成設計: 競合より網羅的・正確な構成を設計する
5. 執筆: CLAUDE.mdの全ルールに従って書く

参考元の記事を丸写ししない。テーマを渡した元のソースには言及しない。

## Search Console 分析スキル

「サーチコンソール分析して」「GSC分析」「Search Console」などのリクエスト＋CSV添付で発動。
スキルファイル: `~/.claude/skills/search-console-analysis/SKILL.md`
