#!/usr/bin/python3
""" Python script that get the attribute X-Request-Id of URL from  line """

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print("{}".format(response.headers['X-Request-Id']))
