(function() {
  'use strict';
  var input = document.getElementById('site-search-input');
  var results = document.getElementById('site-search-results');
  if (!input || !results) return;
  var index = null, loading = null, debounceTimer = null;

  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (loading) return loading;
    loading = fetch('/search-index.json', { cache: 'force-cache' })
      .then(function(r) { return r.json(); })
      .then(function(data) { index = data; return data; })
      .catch(function(e) { loading = null; throw e; });
    return loading;
  }

  input.addEventListener('focus', loadIndex, { once: true });
  input.addEventListener('input', function(e) {
    clearTimeout(debounceTimer);
    var q = e.target.value.trim();
    if (!q) { hide(); return; }
    debounceTimer = setTimeout(function() { runSearch(q); }, 120);
  });
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') { input.value = ''; hide(); input.blur(); }
  });
  document.addEventListener('click', function(e) {
    if (!input.contains(e.target) && !results.contains(e.target)) hide();
  });

  function hide() { results.hidden = true; results.innerHTML = ''; }

  function runSearch(q) {
    loadIndex().then(function(data) {
      var ql = q.toLowerCase();
      var hits = [];
      for (var i = 0; i < data.length; i++) {
        var r = data[i];
        var score = scoreOf(r, ql);
        if (score > 0) hits.push({ r: r, s: score });
      }
      hits.sort(function(a, b) { return b.s - a.s; });
      render(hits.slice(0, 12), q);
    }).catch(function() {
      results.innerHTML = '<div class="sr-empty">検索インデックスの読み込みに失敗しました</div>';
      results.hidden = false;
    });
  }

  function scoreOf(r, ql) {
    var score = 0;
    if ((r.t || '').toLowerCase().indexOf(ql) >= 0) score += 100;
    if ((r.d || '').toLowerCase().indexOf(ql) >= 0) score += 40;
    if ((r.k || '').toLowerCase().indexOf(ql) >= 0) score += 30;
    if ((r.b || '').toLowerCase().indexOf(ql) >= 0) score += 10;
    return score;
  }

  function render(hits, q) {
    if (hits.length === 0) {
      results.innerHTML = '<div class="sr-empty">「' + esc(q) + '」に該当する記事はありません</div>';
    } else {
      var html = '';
      for (var i = 0; i < hits.length; i++) {
        var r = hits[i].r;
        var isGlossary = r.u.indexOf('glossary/') === 0;
        var label = isGlossary ? '用語集' : '記事';
        html += '<a class="sr-item" href="/' + r.u + '">';
        html += '<span class="sr-tag sr-tag-' + (isGlossary ? 'glossary' : 'article') + '">' + label + '</span>';
        html += '<span class="sr-title">' + highlight(r.t || '', q) + '</span>';
        var snippet = excerpt(r.d || r.b || '', q);
        if (snippet) html += '<span class="sr-snippet">' + snippet + '</span>';
        html += '</a>';
      }
      results.innerHTML = html;
    }
    results.hidden = false;
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function(c) {
      return { '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c];
    });
  }
  function highlight(text, q) {
    if (!q) return esc(text);
    var t = String(text);
    var idx = t.toLowerCase().indexOf(q.toLowerCase());
    if (idx < 0) return esc(t);
    return esc(t.slice(0, idx)) + '<mark>' + esc(t.slice(idx, idx + q.length)) + '</mark>' + esc(t.slice(idx + q.length));
  }
  function excerpt(text, q) {
    var t = String(text);
    var idx = t.toLowerCase().indexOf(q.toLowerCase());
    if (idx < 0) return esc(t.slice(0, 80)) + (t.length > 80 ? '…' : '');
    var start = Math.max(0, idx - 30);
    var end = Math.min(t.length, idx + q.length + 70);
    var s = t.slice(start, end);
    var head = start > 0 ? '…' : '';
    var tail = end < t.length ? '…' : '';
    return head + highlight(s, q) + tail;
  }
})();
