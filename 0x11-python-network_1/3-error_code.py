#!/usr/bin/python3
""" Python script that capture the error from URL of command line """

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            data = response.read()
            print("{}".format(data.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
