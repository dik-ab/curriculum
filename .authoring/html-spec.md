# HTML版（マスターコース）変換規約

出力先: `/Users/daiki/sns/master-course/`。Jekyllに依存しない**純粋な静的HTML/CSS**のサイト。ビルド不要でブラウザで直接開けること。

## ディレクトリ構成

```
master-course/
├── index.html                 ← コーストップ（章カード一覧）
├── assets/css/style.css       ← 共通CSS（作成済み。変更しない）
├── 01-environment/            ← 環境構築
├── 02-html-css/               ← HTML/CSS基礎
├── 03-javascript/             ← JavaScript基礎
├── 04-typescript/             ← TypeScript基礎
├── 05-git/
├── 06-react/
├── 07-backend/
├── 08-docker/
├── 09-database/
├── 10-todo/                   ← 実践: フルスタックTodoアプリ（Jekyll版 fullstack-todo/）
├── 11-tooling/
├── 12-testing/
├── 13-cicd/
├── 14-aws/
├── 15-realtime/
├── 16-ai/
├── 17-ai-chat/
└── 18-sns/
```

各章ディレクトリには `index.html`（章の概要＋ページ一覧）と、Jekyll版と同じベース名のページ（例: `what_is_react.html`）を置く。01〜04章はJekyll版の既存コンテンツ（environment/, frontend/, typescript/）を元に再構成する（02はhtml_css.md+html_css_practice.md、03はjavascript*.md、04はtypescript/）。

## ページテンプレート（必ずこの骨格を使う）

```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>ページ名 | プログラミングマスターコース</title>
  <link rel="stylesheet" href="../assets/css/style.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/styles/github.min.css" />
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <a class="course-title" href="../index.html">プログラミングマスターコース</a>
    <div class="chapter-label">第N章 章タイトル</div>
    <nav>
      <h2>この章のページ</h2>
      <ul>
        <li><a href="index.html">章の概要</a></li>
        <li><a href="page1.html" class="current">ページ1</a></li>
        <!-- 章内全ページ。現在ページに class="current" -->
      </ul>
      <h2>コース全体</h2>
      <ul>
        <li><a href="../index.html">コース目次へ戻る</a></li>
      </ul>
    </nav>
  </aside>
  <main class="main">
    <h1>ページ名</h1>
    <!-- 本文 -->
    <nav class="pager">
      <a href="prev.html"><span class="pager-label">← 前のページ</span>前ページ名</a>
      <a href="next.html" class="pager-next"><span class="pager-label">次のページ →</span>次ページ名</a>
    </nav>
  </main>
</div>
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true, theme: "default" });
</script>
</body>
</html>
```

## コンテンツのHTML表現（Jekyll版Markdownとの対応）

| Markdown | HTML |
|---|---|
| `## 学習目標` + リスト | `<div class="box box-goal"><p class="box-title">学習目標</p><ul>…</ul></div>` |
| コードブロック | `<pre><code class="language-typescript">…</code></pre>`（**HTMLエスケープ必須**: `<`→`&lt;` `>`→`&gt;` `&`→`&amp;`） |
| ファイル名表記 | コード直前に `<span class="filename">src/main.ts</span>` |
| コード解説 | `<div class="code-explain"><p class="box-title">コード解説</p><ul>…</ul></div>` |
| ```mermaid ブロック | `<pre class="mermaid">…（エスケープ不要、そのまま）</pre>` |
| 注意書き | `<div class="box box-warning"><p class="box-title">注意</p>…</div>` |
| ポイント | `<div class="box box-point"><p class="box-title">ポイント</p>…</div>` |
| 理解度チェックの解答 | `<details class="quiz"><summary>解答を見る</summary>…</details>` |
| セルフレビュー `- [ ]` | `<ul class="checklist"><li><label><input type="checkbox" />項目</label></li></ul>` |

## リンク

- 章内: `page.html`、他章: `../06-react/setup.html` のような相対パス。
- Jekyll版のリンクをHTML版のディレクトリに読み替える。対応表:

| Jekyll版 | HTML版 |
|---|---|
| `environment/` | `01-environment/` |
| `frontend/html_css.html`, `frontend/html_css_practice.html` | `02-html-css/`（同ファイル名） |
| `frontend/javascript.html`, `frontend/javascript_basics.html`, `frontend/javascript_practice.html` | `03-javascript/`（同ファイル名） |
| `typescript/` | `04-typescript/` |
| `final_project.html` | `04-typescript/final_project.html`（第4章の最終ページとして収録） |
| `git/` | `05-git/` |
| `react/` | `06-react/` |
| `backend/` | `07-backend/` |
| `docker/` | `08-docker/` |
| `database/` | `09-database/` |
| `fullstack-todo/` | `10-todo/` |
| `tooling/` | `11-tooling/` |
| `testing/` | `12-testing/` |
| `cicd/` | `13-cicd/` |
| `aws/` | `14-aws/` |
| `realtime/` | `15-realtime/` |
| `ai/` | `16-ai/` |
| `ai-chat/` | `17-ai-chat/` |
| `sns/` | `18-sns/` |

- `practice/`（回答コード）へのリンクはGitHubリポジトリの絶対URL `https://github.com/dik-ab/curriculum/tree/main/practice/...` に置き換える。
- リンク切れを作らない。存在するファイルにのみリンクする。

## 内容の整合性

- **内容はJekyll版と同一**であること（言い回しの微調整は可、情報の増減は不可）。Jekyll版のMarkdownを読み、それを上記HTML表現に忠実に変換する。
- 文体・構成ルールは `spec.md` と同じ。
