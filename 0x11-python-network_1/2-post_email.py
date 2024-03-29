#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
