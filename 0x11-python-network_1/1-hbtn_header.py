#!/usr/bin/python3
"""
This script takes a URL as a command-line argument nd sends a request to d URL.
It retrieves the value of the 'X-Request-Id' header frm d response to display.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
