#!/bin/bash

# set -x
set -e

# use credentials from env
git remote set-url origin https://${GITHUB_USER}:${GITHUB_OAUTH_TOKEN}@github.com/${GITHUB_USER}/powEUr.git

git pull

exec "$@"
