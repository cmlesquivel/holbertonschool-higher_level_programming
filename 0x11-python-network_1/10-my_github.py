#!/usr/bin/python3
"""   Python script that takes in a letter and sends a POST request """

import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    try:
        response = requests.get(url, auth=(user, passsword))
        my_dict = response.json()
        print("{}".format(my_dict['id']))
    except:
        pass
