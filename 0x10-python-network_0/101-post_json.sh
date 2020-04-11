#!/bin/bash
# Bash script that sends a json File
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
