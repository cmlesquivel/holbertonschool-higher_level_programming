#!/bin/bash
# Bash script that show pages with states code 200
curl -X GET -Li "$1" -s | grep -A 1000 "200 OK" | grep -vP '\S' -A 10 | sed '2q;d'
