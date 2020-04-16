#!/usr/bin/python3
"""Python script that send a POST request to URL from line """

from urllib import parse
from urllib import request
import sys

if __name__ == "__main__":
    try:
        query_args = {'email': sys.argv[2]}
        encoded_args = parse.urlencode(query_args).encode('utf-8')
        url = sys.argv[1]
        print(request.urlopen(url, encoded_args).read().decode('utf-8'))
    except Exception as e:
        print(e)
