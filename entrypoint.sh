#!/bin/bash

# set -x
set -e

./scripts/init-git-config.sh

# cron reset env
env > /etc/environment

# https://stackoverflow.com/questions/43802109/output-of-tail-f-at-the-end-of-a-docker-cmd-is-not-showing/43807880#43807880
echo > /var/log/cron.log

# for python server
mkdir /tmp/foobar

exec "$@"
