#!/usr/bin/python3
""" Python script that get the attribute X-Request-Id of URL
from  line command """

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.getheader('X-Request-Id'))
    except:
        pass
