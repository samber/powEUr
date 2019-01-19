#!/bin/bash

# set -x
set -e

git add data/
git commit -m "Adding $(date +%Y-%m-%d) data"
git push
