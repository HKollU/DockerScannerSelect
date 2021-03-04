#!/bin/bash
curl -i -s -k -X $'GET' \
    -H $'Host: '"$1" -H $'Connection: close' \
    $"$1"'/robots.txt' >robots.txt && cat robots.txt
