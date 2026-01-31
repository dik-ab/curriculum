# プログラミング学習カリキュラム

このリポジトリは、プログラミング学習のための環境構築ガイドを提供しています。

## GitHub Pagesでの表示

https://dik-ab.github.io/curriculum/

## ローカルでプレビューする方法

### 初回セットアップ

```bash
# 1. Rubyがインストールされているか確認
ruby -v

# 2. Bundlerをインストール（まだの場合）
gem install bundler

# 3. 依存関係をインストール
bundle install
```

### サーバーの起動

```bash
# 簡単な方法（推奨）
./serve.sh

# または手動で
bundle exec jekyll serve --config _config.yml,_config_local.yml
```

ブラウザで http://localhost:4000 にアクセスしてください。

## ファイル構成

- `_config.yml` - GitHub Pages用のJekyll設定
- `_config_local.yml` - ローカルプレビュー用の設定（remote_themeを無効化）
- `serve.sh` - ローカルプレビュー起動スクリプト
- `environment/` - 環境構築ガイド
  - `mac_vscode.md` - Mac版 VS Code セットアップ
  - `windows_vscode.md` - Windows版 VS Code セットアップ
  - `live_preview.md` - 拡張機能のセットアップ
  - `init.md` - 初期設定（タイピング練習）
