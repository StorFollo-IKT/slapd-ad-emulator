#!/bin/sh


mkdir -p /tmp/slapd
#ls -l .
#php build_config.php

set -x
exec slapd -f /root/slapd.conf -d1
