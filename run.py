#! /usr/bin/env python3

import os
import requests

directory = 'supplier-data/descriptions/'                         # Directory of the feedback files

keys = ['name', 'weight', 'description', 'image_name']            # List of keys
for filename in os.listdir(directory):
    infile = os.path.join(directory, filename)                    # Filename appended with its directory

    # Read each line of the file
    with open(infile, 'r') as f:
        contents = f.readlines()

    # Process each line of the file to a dictionary
    fruit_dictionary = {}
    fruit_dictionary['name'] = contents[0]
    fruit_dictionary['weight'] = int(contents[1].strip(' lbs\n'))
    fruit_dictionary['description'] = contents[2]
    fruit_dictionary['image_name'] = filename.strip('.txt') + '.jpeg'
    response = requests.post('http://34.70.118.12/fruits/', data=fruit_dictionary)     # Make POST request to the URL

    # Check out the response status
    print(response.status_code)
    print(response.request.url)
    print(response.request.body, end='\n\n')
