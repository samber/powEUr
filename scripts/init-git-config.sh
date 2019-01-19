#!/bin/bash

git config --global user.email "dev@samuel-berthe.fr"
git config --global user.name "Samuel Berthe"

git reset --hard

# use credentials from env
git remote set-url origin https://${GITHUB_USER}:${GITHUB_OAUTH_TOKEN}@github.com/${GITHUB_USER}/powEUr.git

git pull
