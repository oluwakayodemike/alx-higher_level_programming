#!/usr/bin/python3
"""
This script takes a URL as a command-line argument and sends a request to the URL. 
It retrieves the value of the 'X-Request-Id' header from the response and displays it.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
