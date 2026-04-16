# -*- coding: utf-8 -*-
import re

# ===== 1. ec-business-camera.html 作成 =====
# (HTMLは別途作成済み — このスクリプトではindex/archive/sitemap/llms/first-cameraの更新のみ)

# ===== 2. sitemap.xml 更新 =====
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()
new_url = '''  <url>
    <loc>https://tsubasa-memo.github.io/ec-business-camera.html</loc>
    <lastmod>2026-04-16</lastmod>
    <changefreq>monthly</changefreq>
  </url>
</urlset>'''
content = content.replace('</urlset>', new_url)
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(content)
print('2. sitemap.xml 更新完了')

# ===== 3. archive.html 更新（カメラカテゴリの先頭に追加） =====
with open('archive.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_card = '''<div class="article-card" data-cat="camera">
<a href="ec-business-camera.html">
<div class="card-thumb"><img src="thumbs/ec-business-camera.svg" alt="EC担当者向けカメラの選び方" width="320" height="180"></div>
<div class="card-body">
<div class="card-dates"><span class="card-date-pub">公開 2026.04.16</span></div>
<h2>EC担当者向けカメラの選び方｜社内稟議を通す基準と業務用ミラーレスの価格帯</h2>
<p class="card-desc">EC・広報担当が社内稟議を通してカメラを買うときの選定基準。APS-Cエントリー機12〜18万円の5機種比較と、減価償却・費用対効果など稟議6つのチェックポイント。</p>
<span class="card-tag">カメラ</span>
</div>
</a>
</div>
'''
# カメラカテゴリの最初の記事（megapixel-myth）の前に挿入
content = content.replace(
    '<div class="article-card" data-cat="camera">\n<a href="megapixel-myth.html">',
    new_card + '<div class="article-card" data-cat="camera">\n<a href="megapixel-myth.html">',
    1
)
with open('archive.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('3. archive.html 更新完了')

# ===== 4. llms.txt 更新 =====
with open('llms.txt', 'r', encoding='utf-8') as f:
    content = f.read()
new_line = '\n- [EC担当者向けカメラの選び方｜社内稟議を通す基準と業務用ミラーレスの価格帯](https://tsubasa-memo.github.io/ec-business-camera.html): EC・広報担当が社内稟議を通してカメラを買うときの選定基準。APS-Cエントリー機12〜18万円の5機種比較と、減価償却・費用対効果など稟議6つのチェックポイントをまとめた記事'
# カメラセクションの末尾に追加（llms.txtのカメラセクションの最後のエントリを探す）
# まずカメラセクションの構造を確認して適切な場所に挿入
content = content.replace(
    'プラットフォーム依存リスクを整理した記事',
    'プラットフォーム依存リスクを整理した記事' + new_line
)
with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print('4. llms.txt 更新完了')

# ===== 5. index.html 更新 =====
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 5-1: 記事件数 76 → 77
content = content.replace('全76件', '全77件')

# 5-2: PIXTAカードのNEWラベルを日付に変更
content = content.replace(
    '<span class="card-date">NEW</span><span class="card-tag">副業・キャリア</span>',
    '<span class="card-date">2026.04.14</span><span class="card-tag">副業・キャリア</span>'
)

# 5-3: 新記事カードをPIXTAの前に挿入
new_article_card = '''    <div class="article-card">
      <a href="ec-business-camera.html">
        <div class="card-thumb-sm"><img src="thumbs/ec-business-camera.svg" alt="EC担当者向けカメラの選び方" width="140" height="96"></div>
        <div class="card-body">
          <div class="card-meta"><span class="card-date">NEW</span><span class="card-tag">カメラ</span></div>
          <h2>EC担当者向けカメラの選び方｜社内稟議を通す基準と業務用ミラーレスの価格帯</h2>
          <p class="card-desc">EC・広報担当が社内稟議を通してカメラを買うときの選定基準。APS-Cエントリー機12〜18万円の5機種比較と、減価償却・費用対効果など稟議6つのチェックポイント。</p>
        </div>
      </a>
    </div>

'''
content = content.replace(
    '    <div class="article-card">\n      <a href="stockphoto-ai-sidejob.html">',
    new_article_card + '    <div class="article-card">\n      <a href="stockphoto-ai-sidejob.html">',
    1
)

# 5-4: 末尾のllms-txt-setupカードを削除（8件→8件を維持するため）
old_last_card = '''    <div class="article-card">
      <a href="llms-txt-setup.html">
        <div class="card-thumb-sm"><img src="thumbs/llms-txt-setup.svg" alt="llms.txtの設置方法" width="140" height="96"></div>
        <div class="card-body">
          <div class="card-meta"><span class="card-date">2026.04.09</span><span class="card-tag">ブログ運営・SEO</span></div>
          <h2>llms.txtとは何か｜AIにブログを読ませるためのファイル設置</h2>
          <p class="card-desc">llms.txtの仕様・書き方・設置手順・robots.txtとの違い・効果確認の方法をまとめた備忘録。</p>
        </div>
      </a>
    </div>'''
content = content.replace(old_last_card, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('5. index.html 更新完了')

# ===== 6. first-camera.html 修正 =====
with open('first-camera.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 6-1: 壊れたAmazon商品画像タグを5箇所すべて削除
old_pattern = re.compile(r'  <img src="https://images-na\.ssl-images-amazon\.com/images/I/41vwOXXSXSL\._SL160_\.jpg" alt="[^"]*" class="amazon-card-img">\n')
c1 = len(old_pattern.findall(html))
html = old_pattern.sub('', html)

# 6-2: Nikon Z30 → Nikon Z50
c2 = html.count('<td>Nikon Z30</td>')
html = html.replace('<td>Nikon Z30</td>', '<td>Nikon Z50</td>')

# 6-3: メルカリ・ヤフオクセクション削除
old_section = '''<h3>フリマアプリやオークションは避けるべき？</h3>

<p>メルカリやヤフオクでは専門店より安い価格でカメラが出品されています。ただし初心者には以下のリスクがあります。</p>

<p>まず、商品状態の見極めが難しい点。カメラの「外観はきれい」でも、センサーにホコリがあったり、AFの精度が落ちていたりといった問題は写真だけではわかりません。次に、保証がない点。個人間取引なので初期不良があっても返品できないケースが多いです。最後に、偽物や盗品のリスク。数は少ないですが、ゼロではありません。</p>

<p>中古カメラに慣れて、ある程度自分で状態を判断できるようになってからフリマアプリに挑戦するのが安全です。最初の1台は専門店の保証付き商品をおすすめします。</p>

'''
c3 = 1 if old_section in html else 0
html = html.replace(old_section, '')

# 6-4: 終了済みセール告知削除
old_sale_box = '''<div class="point-box" style="background:#fff8e8;border-color:#f0a500;">
<strong>\U0001f4e6 Amazon新生活セールFinal開催中（3/31〜4/6）</strong><br>
カメラ・レンズがセール対象になることがあります。下記の商品リンクから現在の価格を確認してみてください。
</div>

'''
c4 = 1 if old_sale_box in html else 0
html = html.replace(old_sale_box, '')

with open('first-camera.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'6. first-camera.html 修正完了（画像{c1}箇所、typo{c2}箇所、メルカリ{c3}ブロック、セール{c4}ブロック）')

print('\n全更新完了')
