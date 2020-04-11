#!/bin/bash
# Bash script that get only status code
curl -sL -w "%{http_code}" -I "$1" -o /dev/null
