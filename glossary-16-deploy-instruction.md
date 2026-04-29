# 用語集16本追加 - 周辺ファイル更新指示

以下の16本の用語集HTMLは `glossary/` ディレクトリに配置済みの前提。周辺ファイルを更新してコミットまで。

追加されたファイル:
- glossary/jpeg.html
- glossary/raw.html
- glossary/color-correction.html
- glossary/skin-retouch.html
- glossary/compositing.html
- glossary/contrast.html
- glossary/color-temperature.html
- glossary/white-balance.html
- glossary/exposure.html
- glossary/lighting.html
- glossary/sasage.html
- glossary/crowdsourcing.html
- glossary/portfolio.html
- glossary/tax-return.html
- glossary/crawler.html
- glossary/internal-link.html

## 更新対象

### 1. sitemap.xml
16件のURLを追加（`<changefreq>monthly</changefreq>`、`<lastmod>2026-04-27</lastmod>`）:
```
glossary/jpeg.html
glossary/raw.html
glossary/color-correction.html
glossary/skin-retouch.html
glossary/compositing.html
glossary/contrast.html
glossary/color-temperature.html
glossary/white-balance.html
glossary/exposure.html
glossary/lighting.html
glossary/sasage.html
glossary/crowdsourcing.html
glossary/portfolio.html
glossary/tax-return.html
glossary/crawler.html
glossary/internal-link.html
```

### 2. glossary/index.html
用語集トップページの一覧に16件を追加。既存のカテゴリ分類に合わせて以下の通り配置:

- 画像フォーマット系: JPEG、RAW
- レタッチ系: 色補正、肌補正、合成、コントラスト
- カメラ・撮影系: 色温度、ホワイトバランス、露出、ライティング
- EC実務系: ささげ業務
- 副業・キャリア系: クラウドソーシング、ポートフォリオ、確定申告
- SEO系: クローラー、内部リンク

### 3. llms.txt
16件のエントリを追加。形式は既存エントリに合わせる。

### 4. search-index.json
```bash
python3 build_search_index.py
```

### 5. index.html
記事件数表示を更新（+16件）。archive.htmlの実際のカード数と同期させる。

### 6. archive.html
用語集セクションに16件追加（既存の用語集カードのフォーマットに合わせる）。

```bash
git add -A
git commit -m "用語集16本追加（JPEG・RAW・色補正・肌補正・合成・コントラスト・色温度・ホワイトバランス・露出・ライティング・ささげ業務・クラウドソーシング・ポートフォリオ・確定申告・クローラー・内部リンク）"
```
