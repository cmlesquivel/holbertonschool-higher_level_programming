#!/usr/bin/python3
"""  Python script that capture the error from URL of command line  """

import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print("{}".format(response.text))
    except Exception as e:
        print("Error code: {}".format(response.status_code))
