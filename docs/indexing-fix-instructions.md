# Claude Code指示書：インデックス改善作業

## やること一覧

### 1. sitemap.xml を最新版で上書き
添付の `sitemap.xml` でリポジトリの `sitemap.xml` を上書きする。
全18ページ（トップ + archive + 記事16本）が含まれている。

### 2. robots.txt を配置
添付の `robots.txt` をリポジトリのルート（index.htmlと同じ場所）に配置する。
既にあれば上書き。

### 3. exif-info.html のtitle・meta descriptionを変更

**titleタグ：**
```
変更前：写真のExif情報とは？位置情報のリスクと削除方法まとめ【2026年版】
変更後：X（Twitter）に写真の位置情報は残る？Exif確認・削除方法まとめ【2026年版】
```

**meta description：**
```
変更前：Exifに含まれる情報、SNSごとの自動削除状況、iPhone/Android/PC別の削除手順をまとめました。
変更後：X（旧Twitter）やInstagramに投稿した写真の位置情報は大丈夫？Exif情報の中身、SNSごとの自動削除状況、iPhone・Android・PCでの確認・削除手順をまとめました。
```

**og:titleも変更：**
```
変更後：X（Twitter）に写真の位置情報は残る？Exif確認・削除方法まとめ
```

※ h1タグは変更しない。

### 4. retouch-apps.html にセクション追加 + title微修正

**titleタグ：**
```
変更前：スマホで写真レタッチ！初心者向け無料アプリおすすめ10選【2026年版】
変更後：スマホで写真レタッチ・色補正！無料アプリおすすめ10選【2026年版】
```

**本文にセクション追加（Snapseedセクションの後に挿入）：**

```html
<h3>写真の色補正・再色付けにはどのアプリが向いている？</h3>

<p>「写真の再色付け」という言葉で検索する人が増えているようだが、これは要するに色味の補正のこと。撮影時にホワイトバランスがずれて青っぽく・オレンジっぽくなった写真を自然な色に戻したり、古い写真の褪せた色を鮮やかにしたりする作業を指す。</p>

<p>この用途に向いているアプリは以下の通り。</p>

<p><strong>Snapseed</strong>のホワイトバランスツールを使えば、色温度と色合いをスライダーで直感的に調整できる。「この写真、ちょっと青い」と感じたら色温度を暖かい方向に動かすだけ。完全無料で広告もない。</p>

<p><strong>Adobe Lightroom Mobile</strong>は色補正の精度が一段高い。HSL（色相・彩度・輝度）パネルで特定の色だけを狙って調整できるので、「肌の色は変えずに空の青だけ濃くしたい」といった細かい調整が可能。無料版でもHSL調整は使える。</p>

<p><strong>PhotoDirector</strong>にはAI自動カラー補正があり、ワンタップで色味を最適化してくれる。手動調整が面倒な人向け。</p>

<p>古い写真の本格的な色復元（セピア調の写真をフルカラーに変換するなど）は、アプリだけでは限界がある。<a href="retouch-services.html">プロのレタッチサービス</a>に依頼したほうが確実。</p>
```

### 5. mainブランチに直接push

今回はインデックス改善が目的なので、draft予約ではなくmainに直接pushする。

```bash
git add sitemap.xml robots.txt exif-info.html retouch-apps.html
git commit -m "fix: インデックス改善（sitemap.xml更新・title最適化・コンテンツ追加）"
git push origin main
```
