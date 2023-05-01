#!/bin/bash
# script must send a POST request with the contents of a file, passed with
# the filename as the second argument of the script, in the body of the
# request.
curl - sX POST - H "Content-Type: application/json" - d @ "$2" "$1"
