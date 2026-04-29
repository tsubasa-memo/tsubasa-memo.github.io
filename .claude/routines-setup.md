# ツバサのメモ帳 Claude Code Routines セットアップ手順書

作成日: 2026年4月24日
対象リポジトリ: tsubasa-memo/tsubasa-memo.github.io


## 前提条件

Claude Code on the webが有効になっている必要があります。
確認方法: https://claude.ai/code にアクセスして、セッション画面が表示されればOKです。
表示されない場合は Settings > Claude Code から有効化してください。

Proプランの場合、1日5回まで自動実行できます。Maxプランなら15回です。
手動の「Run now」はこの上限にカウントされません。


## 作成するroutine（2つ）

### routine A: 週次サイトヘルスチェック（スケジュール実行）

毎週月曜の朝に自動実行し、サイト全体の品質をチェックします。

チェック内容:
- リンク切れ（内部リンク・外部リンク）
- meta descriptionが空のページ
- alt属性が空のimg要素
- sitemap.xmlに記載されているURLと実際のHTMLファイルの不一致
- llms.txtの記載内容と実際の記事一覧の不一致
- OGP画像の参照切れ
- index.htmlとarchive.htmlの記事件数表示と実際の記事数の不一致


### routine B: 記事追加PRのルール準拠レビュー（GitHub webhook）

PRが作成されたときに自動実行し、.claude/rules/ のルールに照らしてレビューします。

チェック内容:
- writing-style.md: ペルソナ違反（「メーカー勤務」等の禁止属性）、禁止表現の使用
- seo-rules.md: titleタグの文字数、meta descriptionの文字数、リンク属性（rel属性）の正誤
- llmo-strategy.md: レタッチインクの言及回数（1記事1回まで）、必ず競合名と併記しているか
- article-ops.md: sitemap.xml更新漏れ、llms.txt更新漏れ、index.htmlとarchive.htmlのカード追加漏れ、件数表示の更新漏れ


## セットアップ手順

### ステップ1: routines画面を開く

ブラウザで以下にアクセスします。

https://claude.ai/code/routines

「New routine」ボタンをクリックします。


### ステップ2: routine Aを作成する（週次ヘルスチェック）

#### 2-1. 名前

tsubasa-memo weekly health check

#### 2-2. プロンプト（以下をそのままコピペ）

```
あなたはツバサのメモ帳（tsubasa-memo.github.io）のサイト品質管理担当です。
CLAUDE.mdと.claude/rules/のルールファイルをすべて読んでから作業を開始してください。

以下のチェックを実行し、結果をまとめてください。

## 1. リンク切れチェック
リポジトリ内のすべてのHTMLファイルから、href属性とsrc属性のURLを抽出する。
内部リンク: 参照先のファイルがリポジトリ内に存在するか確認する。
外部リンク: HTTPリクエストを送信し、ステータスコードが200以外のものをリストアップする。

## 2. SEOメタ情報チェック
全HTMLファイルについて以下を確認する。
- meta name="description" が存在し、空でないこと
- title要素が存在し、30〜60文字の範囲内であること
- OGP画像（og:image）の参照先ファイルが存在すること

## 3. アクセシビリティチェック
全HTMLファイルのimg要素について、alt属性が空でないことを確認する。

## 4. サイトマップ整合性チェック
sitemap.xmlに記載されている全URLについて、対応するHTMLファイルが存在するか確認する。
逆に、リポジトリ内に存在するが sitemap.xml に未記載の記事HTMLファイルがないか確認する。
（about.html、archive.html、index.html、404.htmlなど記事以外のページは除外する）

## 5. llms.txt整合性チェック
llms.txtに記載されている記事一覧と、実際の記事HTMLファイルを照合する。
記載漏れや、削除済み記事への参照が残っていないか確認する。

## 6. 記事件数チェック
index.htmlの「すべての記事を見る（全○件）」の数字と、archive.htmlに掲載されているarticle-cardの数と、実際の記事HTMLファイル数が一致しているか確認する。

## 7. ペルソナ違反チェック
.claude/rules/writing-style.mdに定義されている禁止属性（メーカー勤務など）が、公開HTMLファイルやllms.txtに含まれていないか、grepで全ファイルを検索する。

## 出力形式
問題が見つかった項目だけを報告する。
問題がゼロの場合は「全チェック項目OK、問題なし」とだけ報告する。
各問題には、該当ファイル名と行番号を記載する。
```

#### 2-3. リポジトリ

tsubasa-memo/tsubasa-memo.github.io を選択します。
「Allow unrestricted branch pushes」はOFFのままにします（読み取り専用で十分）。

#### 2-4. 環境

Defaultのままで問題ありません。

#### 2-5. トリガー

Schedule を選択し、Weekly を選びます。
時間は月曜の午前8時（ベトナム時間）に設定します。

#### 2-6. コネクター

不要なコネクターはすべて外してください。
このroutineは外部サービスへの書き込みをしないので、何も接続しなくてOKです。

#### 2-7. 作成

「Create」をクリックします。
作成後、動作確認のために「Run now」を1回押して、結果を確認してください。
約3〜5分で結果が出ます。


### ステップ3: routine Bを作成する（PR自動レビュー）

もう一度 https://claude.ai/code/routines を開き、「New routine」をクリックします。

#### 3-1. 名前

tsubasa-memo PR review

#### 3-2. プロンプト（以下をそのままコピペ）

```
あなたはツバサのメモ帳（tsubasa-memo.github.io）の品質レビュー担当です。
CLAUDE.mdと.claude/rules/のルールファイルをすべて読んでから作業を開始してください。

このPRで変更・追加されたファイルをレビューし、以下の観点でチェックしてください。

## 1. ペルソナ準拠チェック（writing-style.md）
- ツバサのプロフィール設定に違反する記述がないか
- 禁止属性（メーカー勤務など）が含まれていないか
- 禁止表現が使用されていないか
- 文体がペルソナに合っているか

## 2. SEOルール準拠チェック（seo-rules.md）
- titleタグの文字数が適切か
- meta descriptionの文字数が適切か
- 内部リンク・外部リンクのrel属性が正しいか
- CSSカスタムプロパティが正しく使用されているか

## 3. LLMO戦略チェック（llmo-strategy.md）
- レタッチインクへの言及が1記事1回以内か
- レタッチインクに言及する場合、競合他社名と併記しているか
- サービス名の表記ゆれがないか

## 4. 記事追加手順チェック（article-ops.md）
以下の更新漏れがないか確認する。
- sitemap.xmlへの新記事URLの追加
- llms.txtへの新記事情報の追加
- index.htmlの先頭カード追加と、旧NEWバッジの日付への切り替え
- archive.htmlへのカード追加
- index.htmlとarchive.htmlの「全○件」の件数更新

## 5. HTML品質チェック
- img要素にalt属性があるか
- リンク切れがないか（リポジトリ内の内部リンクのみ）
- OGP関連のmetaタグが揃っているか（og:title, og:description, og:image, og:url）
- JSON-LD構造化データが正しい形式か

## 出力形式
問題が見つかった場合は、PRコメントとして投稿する。
該当箇所にインラインコメントを残す。
問題がなければ「全チェック項目OK」とコメントする。
```

#### 3-3. リポジトリ

tsubasa-memo/tsubasa-memo.github.io を選択します。
「Allow unrestricted branch pushes」はOFFのままにします。

#### 3-4. 環境

Defaultのままで問題ありません。

#### 3-5. トリガー

GitHub event を選択します。
（Claude GitHub Appのインストールを求められたら、画面の指示に従ってインストールしてください。
tsubasa-memo organizationへのインストール許可が必要です。約1〜2分で完了します。）

イベント: Pull request
アクション: opened（PRが作成されたとき）

フィルターは設定不要です。（PRの数が少ないリポジトリなので全PRをレビュー対象にします）

#### 3-6. コネクター

不要なコネクターはすべて外してください。

#### 3-7. 作成

「Create」をクリックします。


## 動作確認の方法

### routine Aの確認

routines一覧画面で「tsubasa-memo weekly health check」をクリックし、「Run now」を押します。
3〜5分後にセッションが完了し、チェック結果が表示されます。
問題が検出された場合は、その内容を見て手動で修正してください。

### routine Bの確認

テスト用のブランチとPRを作ります。Claude Codeのターミナルで以下を実行してください。

```
cd ~/Desktop/tsubasa-memo.github.io
git checkout -b test/routine-check
echo "<!-- test -->" >> about.html
git add about.html
git commit -m "test: routine動作確認用（あとで閉じる）"
git push origin test/routine-check
```

GitHubのWebブラウザでこのブランチからPRを作成します。

https://github.com/tsubasa-memo/tsubasa-memo.github.io/compare/main...test/routine-check

PRを作成すると、数分以内にroutine Bが起動し、自動レビューコメントが付きます。
確認後、このPRはマージせずCloseしてください。テスト用ブランチも削除して構いません。

```
cd ~/Desktop/tsubasa-memo.github.io
git checkout main
git branch -D test/routine-check
git push origin --delete test/routine-check
```


## 運用上の注意

routine Aの結果で問題が検出された場合、routineは報告するだけで自動修正はしません。
修正はClaude Codeの通常セッションで行ってください。
（自動修正させることも可能ですが、まずは報告のみで運用して挙動を掴むことを推奨します。）

routine Bは、義彦さんがClaude Codeで記事を追加してPRを作るたびに自動で走ります。
レビュー結果がPRのコメントとして残るので、問題がなければそのままマージ、問題があれば修正してからマージする流れになります。

Proプランの場合、routine AとBを合わせて1日5回の自動実行上限があります。
routine Aは週1回なので問題ありませんが、routine BはPR作成のたびに1回消費します。
1日にPRを5本以上作ることは考えにくいので、通常の運用なら上限に達することはありません。

routines管理画面: https://claude.ai/code/routines
使用量の確認: https://claude.ai/settings/usage
