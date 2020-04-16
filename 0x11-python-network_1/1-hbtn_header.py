#!/usr/bin/python3
""" Python script that get the attribute X-Request-Id of URL
from  line command """

import urllib
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    data = response
print(data.getheader('X-Request-Id'))
