#!/bin/bash
# Bash script that sends a POST request
curl "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
