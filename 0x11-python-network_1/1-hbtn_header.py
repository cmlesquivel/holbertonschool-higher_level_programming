#!/usr/bin/python3
""" Python script that get the attribute X-Request-Id of URL from  line """

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        try:
            print(response.headers.get("X-Request-Id"))
        except Exception as e:
            print(e)
