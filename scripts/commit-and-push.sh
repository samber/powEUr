#!/bin/bash

# use credentials from env
git remote set-url origin https://${GITHUB_USER}:${GITHUB_OAUTH_TOKEN}@github.com/${GITHUB_USER}/powEUr.git

git add data/
git commit -m "Adding $(date +%Y-%m-%d) data"
git push
