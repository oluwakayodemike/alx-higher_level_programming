#!/usr/bin/env python3
"""
Python script that takes your GitHub credentials (username and password),
and uses the GitHub API to display your id.
"""
import requests
import sys

if __name__ == '__main__':
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <token>")
        sys.exit(1)

    # Assign arguments to variables
    username = sys.argv[1]
    token = sys.argv[2]

    # Make a GET request to the GitHub API using Basic Auth
    response = requests.get("https://api.github.com/user",
                            auth=(username, token))

    # If the request was successful (200 status code), print the user ID
    if response.status_code == 200:
        print(response.json()['id'])
    # Otherwise, print None
    else:
        print("None")
