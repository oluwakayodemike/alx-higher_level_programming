#!/usr/bin/python3
"""
Sends a POST request with email as parameter to the URL passed as argument
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
