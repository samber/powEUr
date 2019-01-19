#!/bin/bash

# set -x
set -e

./scripts/init-git-config.sh

# cron reset env
env > /etc/environment

# outputing jobs logs
# 🤮
tail -f /var/log/cron.log &

exec "$@"
