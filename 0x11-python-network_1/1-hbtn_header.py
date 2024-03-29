#!/usr/bin/python3
"""
This script takes in a URL, sends a request, and displays the value
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
