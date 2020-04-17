#!/usr/bin/python3
"""   Python script that takes in a letter and sends a POST request """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        aux = sys.argv[1]
    else:
        aux = ''

    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data={'q': aux})
        my_dict = response.json()

        if len(my_dict) > 0:
            print("[{}] {}".format(my_dict['id'], my_dict['name']))
        elif len(my_dict) == 0:
            print("No result")
    except:
        print("Not a valid JSON")
