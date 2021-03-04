#!/bin/bash
curl -i -s -k -X $'GET' \
    -H $'Host: '"$1" -H $'Upgrade-Insecure-Requests: 1' -H $'Accept: */*' -H $'Accept-Language: en-US,en-GB;q=0.9,en;q=0.8' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Connection: close' -H $'Cache-Control: max-age=0' -H $'Accept-Encoding: gzip, deflate' \
    $"$1"'/%3fnkq%26tzb%3d1/' >HTTPPollute.txt && cat HTTPPollute.txt
