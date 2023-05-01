#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1" | grep -q "You got me!" && echo "You got me!" || echo "Something went wrong."
