#!/bin/bash

# set -x
set -e

# in case we pushed code on github
git pull

git add data/
git commit -m "Adding $(date +%Y-%m-%d) data"
git push || git reset --hard
