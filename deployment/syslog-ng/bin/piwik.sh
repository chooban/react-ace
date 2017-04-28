#!/bin/sh

/usr/local/bin/import_logs.py \
 --url=http://piwikapp/ \
 --idsite=1 --recorders=4 --enable-http-errors --enable-http-redirects --enable-static --enable-bots \
 --log-format-name=nginx_json -
