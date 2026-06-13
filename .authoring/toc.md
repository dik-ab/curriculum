# 全体TOC（URLパスとnav_orderの正）

リンクを張るときはこの一覧にあるパスのみ使用する。`/curriculum/` がbaseurlだが、ページ間リンクは相対パスで書くため意識しなくてよい。

## 既存（入門編）

| nav | セクション | パス |
|---|---|---|
| 1 | ホーム | `/` (index.md) |
| 2 | 環境構築 | `/environment/` 配下: mac_vscode.html, windows_vscode.html, live_preview.html, init.html, terminal.html, file_directory.html, node.html |
| 3 | フロントエンド基礎 | `/frontend/` 配下: html_css.html, html_css_practice.html, javascript.html, javascript_basics.html, javascript_practice.html |
| 4 | TypeScript基礎 | `/typescript/` 配下: what_is_typescript.html, hello_world.html, compile.html, basic_types.html, functions.html, practice.html |
| 5 | 入門編最終問題 | `/final_project.html` |

## 新規（中級編＝マスターコース）

### 6. Git/GitHub基礎 — `git/` (title: "Git/GitHub基礎")
- index.md
- what_is_git.md — バージョン管理とは、Gitの仕組み（リポジトリ/コミット/作業ツリー、図）
- basic_commands.md — init/add/commit/status/log/diff、.gitignore
- branch_and_merge.md — ブランチ、マージ、コンフリクト解消
- github_and_pr.md — リモート、push/pull、Pull Request、レビューの流れ（シーケンス図）
- practice.md — 練習問題

### 7. React基礎 — `react/` (title: "React基礎")
- index.md
- what_is_react.md — なぜReactか、SPAとは、仮想DOM（図）
- setup.md — Viteでプロジェクト作成、ディレクトリ構成解説
- jsx_and_components.md — JSX、コンポーネント、関数コンポーネント
- props_and_state.md — props、useState、単方向データフロー（図）
- hooks.md — useEffect、依存配列、カスタムフックの入口
- forms_and_lists.md — フォーム入力、リスト表示とkey、条件付きレンダリング
- api_fetch.md — fetchでAPI通信、ローディング/エラー処理（シーケンス図）
- practice.md — 練習問題（Todoアプリ強化など）

### 8. バックエンド基礎（NestJS） — `backend/` (title: "バックエンド基礎（NestJS）")
- index.md
- http_and_rest.md — HTTP、リクエスト/レスポンス、メソッド、ステータスコード、RESTとは（シーケンス図必須）
- what_is_nestjs.md — なぜNestJSか、アーキテクチャ概観（Module/Controller/Serviceの図）
- setup.md — Nest CLI、プロジェクト作成、ファイル構成解説、起動
- controller.md — ルーティング、パラメータ、クエリ、ボディ
- service_and_di.md — Service、依存性注入（DI）の概念（図）、Module
- dto_and_validation.md — DTO、class-validator、ValidationPipe
- crud_practice.md — メモAPIを作る（CRUD一通り、メモリ上の配列で）
- practice.md — 練習問題

### 9. Docker基礎 — `docker/` (title: "Docker基礎")
- index.md
- what_is_container.md — コンテナとは、VMとの違い（図）、なぜ使うか
- install_and_basics.md — Docker Desktop導入、image/container、run/ps/stop/rm/logs/exec
- dockerfile.md — Dockerfileの書き方（Node.jsアプリを例に、1行ずつ解説）、build、レイヤー（図）
- docker_compose.md — compose.yamlの書き方、複数コンテナ、ボリューム、ネットワーク（図）
- dev_environment.md — 開発環境をcomposeで組む（API+DB）

### 10. データベースとPrisma — `database/` (title: "データベースとPrisma")
- index.md
- what_is_database.md — RDBとは、テーブル/行/列、主キー/外部キー（図）、SQL基礎（SELECT/INSERT/UPDATE/DELETE）
- postgresql_setup.md — composeでPostgreSQL16を起動（→docker参照）、psqlで触る
- prisma_setup.md — Prisma導入、schema.prisma、.env、ディレクトリ構成
- schema_and_migration.md — モデル定義、migrate dev、マイグレーションとは（図）
- crud_with_prisma.md — Prisma ClientでCRUD、NestJSへの組み込み（PrismaService）
- relations.md — 1対多/多対多、include/select、リレーションのクエリ
- practice.md — 練習問題（メモAPIをDB永続化に改造）

### 11. 実践: フルスタックTodoアプリ — `fullstack-todo/` (title: "実践: フルスタックTodoアプリ")
ここまでのReact / NestJS / Prisma / Dockerを総動員する初の通しプロジェクト。RESTの感覚を掴むことが目的。開発環境の標準形（DBはdocker-compose、APIとフロントは `pnpm run dev`）をここで確立する。
- index.md — 作るもの（完成イメージ）、API設計表（エンドポイント一覧）、ER図、構成図
- setup.md — リポジトリ構成（frontend/ backend/ compose.yaml）、DB起動、Prisma初期化（→docker/database参照）
- backend.md — Todo API実装（NestJS+Prisma、CRUD、バリデーション）、curlでの動作確認
- frontend.md — React画面実装（一覧/追加/完了切替/削除）、fetchでAPI接続
- integration.md — つなぎ込みで起きること: CORS、プロキシ設定、エラーハンドリング（シーケンス図）
- practice.md — 拡張課題（期限、絞り込み、編集など）

### 12. コード品質と開発ツール — `tooling/` (title: "コード品質と開発ツール")
- index.md
- prettier.md — フォーマッタとは、Prettier導入、設定、format script
- eslint.md — リンタとは、ESLint導入、ルール、Prettierとの併用
- editor_and_scripts.md — VS Code連携（保存時フォーマット）、pnpm scripts整備

### 13. バックエンドテスト — `testing/` (title: "バックエンドテスト")　※コンパクトに
- index.md — テストはなぜ書くか、テストピラミッド（図）、単体/結合/E2Eの違い
- unit_test.md — Jest基礎（describe/it/expect）、SNSのServiceを例にした単体テスト、モック
- e2e_test.md — supertestによるE2Eテスト、SNSのAPI（投稿・いいね）を例に、テストDB

### 14. CI/CD — `cicd/` (title: "CI/CD")
- index.md
- what_is_cicd.md — CI/CDとは、なぜ必要か（図）
- github_actions_basics.md — workflow/job/step、YAMLの読み方1行ずつ、トリガー
- ci_pipeline.md — lint+test+buildを回すCIを作る（SNSを題材に）
- build_and_deploy_flow.md — ビルドとは何か（tsc/vite buildの成果物）、CDの全体像（図）

### 15. AWSデプロイ — `aws/` (title: "AWSデプロイ")
- index.md — この章の全体像（最終的に作る構成図を先に見せる）
- what_is_aws.md — クラウドとは、AWSとは、リージョン/AZ、アカウント作成、IAM、料金の注意（無料枠・削除手順・予算アラート）
- core_services.md — 各サービスは何をするのか: VPC / S3 / CloudFront / ECR / ECS(Fargate) / ALB / RDS / SES / IAM / Route 53 を「SNSアプリのどの部分を担うか」のマッピング図つきで1つずつ解説
- what_is_iac.md — IaC（Infrastructure as Code）とは、なぜ手作業ではだめか、CDKとTerraformの比較（表+図）、本カリキュラムはCDK採用（TypeScriptで書けるため）、各ページにTerraform対訳例を併記する方針の説明
- cdk_setup.md — CDK導入、cdk init、bootstrap、スタック/コンストラクトの概念（図）、最初のスタック（S3バケット1個）を1行ずつ解説、cdk diff/deploy/destroy
- s3_cloudfront.md — フロントエンドのデプロイ: vite build → S3 → CloudFront（構成図、キャッシュ）。CDKで構築（1行ずつ解説）+ 同じ構成のTerraform例を併記
- ecr_ecs.md — APIのデプロイ: Dockerイメージ → ECR → ECS Fargate + ALB（構成図）。CDKで構築 + Terraform例併記
- rds.md — 本番DB: RDS for PostgreSQL、セキュリティグループ、Secrets Manager。CDKで構築 + Terraform例併記
- ses.md — SESでメール送信: サンドボックス、ドメイン/メール検証、NestJSからの送信実装（SDK v3）
- deploy_from_cicd.md — GitHub ActionsからAWSへ自動デプロイ（OIDC、S3 sync + CloudFront invalidation / ECRプッシュ+ECSサービス更新、cdk deployの自動化）（シーケンス図）

### 16. リアルタイム通信 — `realtime/` (title: "リアルタイム通信")
- index.md
- what_is_realtime.md — ポーリング/SSE/WebSocketの比較（シーケンス図3本）
- websocket_basics.md — WebSocketの仕組み、ハンドシェイク（シーケンス図）、素のWebSocketを試す
- nestjs_gateway.md — NestJS Gateway（Socket.IO）でミニチャットを作る、room、イベント設計

### 17. AI開発入門 — `ai/` (title: "AI開発入門")
- index.md
- what_is_llm.md — LLMとは、トークン、できること/苦手なこと、AIとの付き合い方（図）
- claude_code_setup.md — Claude Code（CLI）の導入、基本操作、許可モード
- claude_md.md — CLAUDE.mdとは何か・なぜ効くか・書き方（良い例/悪い例）
- skills_and_commands.md — スラッシュコマンドとskills、カスタムコマンドの作り方
- ai_pair_programming.md — AIとの実践的な開発フロー（計画→実装→レビュー）、注意点

### 18. AIチャット開発（RAG） — `ai-chat/` (title: "AIチャット開発（RAG）")
- index.md — 作るもの: 「このカリキュラムに質問できるQ&Aボット」（完成図、構成図）
- what_is_rag.md — RAGとは、なぜ必要か、embeddingとベクトル検索（図で直感的に）
- claude_api.md — Claude API基礎、APIキー、Messages API、ストリーミング（最小実装）
- embeddings_and_pgvector.md — embeddingの生成、pgvector導入（→database参照）、類似検索
- build_rag_chat.md — NestJS+pgvector+Claude APIでQ&Aボット構築、Reactのチャット画面（シーケンス図必須）
- practice.md — 改良課題

### 19. SNS開発（最終プロジェクト） — `sns/` (title: "SNS開発（最終プロジェクト）")
- index.md — 要件一覧、画面一覧、ER図、アーキテクチャ図、開発の進め方
- project_setup.md — リポジトリ構成（frontend/backend）、compose、Prisma初期化（→docker/database参照）
- auth.md — ユーザー登録/ログイン、bcrypt、JWT、Guard（ここでGuardを初導入、シーケンス図必須）
- email_verification.md — SESによる登録確認メール（→aws/ses参照）
- posts.md — 投稿のCRUD、タイムライン（自分+全体）
- likes.md — いいね/いいね解除（多対多、→database/relations参照）
- follow.md — フォロー/フォロー解除、フォロー中タイムライン（自己参照多対多）
- chat.md — DMチャット（WebSocket、→realtime参照、シーケンス図）
- profile_and_images.md — プロフィール編集、S3への画像アップロード（presigned URL、シーケンス図）
- testing.md — SNSのテストを書く（→testing参照、代表的な単体+E2E）
- deploy.md — 全体デプロイ（S3/CloudFront + ECS + RDS + CI/CD、→aws/cicd参照）
- wrap_up.md — 総セルフレビュー、追加課題（通知、検索、ページネーション等）

## HTML版（マスターコース単体サイト）

`/Users/daiki/sns/master-course/` に生成。構成は別途 `html-spec.md` を参照。
