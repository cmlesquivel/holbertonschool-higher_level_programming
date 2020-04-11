#!/bin/bash
# Bash script that sends a json File
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
