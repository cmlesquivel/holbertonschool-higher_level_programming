#!/usr/bin/python3
""" Python script that fetches the type and content
of intranet.hbtn/io/status """

import requests

response = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print('\t- content: {}'.format(response.text))
