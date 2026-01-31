#!/bin/bash
# ローカルプレビュー用スクリプト

echo "Starting Jekyll local preview..."
bundle exec jekyll serve --config _config.yml,_config_local.yml
