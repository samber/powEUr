#!/bin/bash

# set -x
set -e

TODAY=$(date +%Y-%m-%d)

ls -d ../data/*/* | xargs -I {} ln -sfrv {}/${TODAY}.json {}/_latest.json
