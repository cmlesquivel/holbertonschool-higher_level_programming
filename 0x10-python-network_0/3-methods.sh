#!/bin/bash
# Bash script that show methods allow
curl -sI "$1" | grep "Allow" | sed 's/Allow: //'
