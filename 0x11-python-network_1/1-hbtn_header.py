#!/usr/bin/python3
""" Python script that get the attribute X-Request-Id of URL
from  line command """

import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response
    print(data.getheader('X-Request-Id'))
except Exception as e:
    print(e)
