#!/usr/bin/env python3

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
directory = "supplier-data/images/"

for filename in os.listdir(directory):
    if filename.endswith('.jpeg'):
        infile = os.path.join(directory, filename)
        with open(infile, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
