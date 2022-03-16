#!/usr/bin/env python3

import os
from PIL import Image

def process_image(filename, directory):
    infile = os.path.join(directory, filename)      # Input file appended with the directory
    outfile = infile.strip('.tiff') + '.jpeg'                      # Output file appended with the directory

    # Image is processed here
    with Image.open(infile) as img:
        img.resize((600, 400)).convert('RGB').save(outfile, 'JPEG')

def main():
    directory = 'supplier-data/images/'    # Images folder
    for filename in os.listdir(directory):
        if filename.endswith('.tiff'):
            try:
                process_image(filename, directory)
            except:
                pass

if __name__ == '__main__':
    main()
