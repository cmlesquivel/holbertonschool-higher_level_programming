#!/usr/bin/python3
""" Python script that send a POST request to URL from line """

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    try:
        query_args = {'email': sys.argv[2]}
        encoded_args = urllib.parse.urlencode(query_args)
        encoded_args = encoded_args.encode('utf-8')
        req = urllib.request.Request(sys.argv[1], encoded_args)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        print(e)
