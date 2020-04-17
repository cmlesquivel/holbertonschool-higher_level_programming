#!/usr/bin/python3
"""  Python script that send a POST request to URL from line """

import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print("{}".format(response.text))
    except Exception as e:
        pass
