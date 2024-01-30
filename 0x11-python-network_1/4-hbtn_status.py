#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    text = requests.get(url).text
    response_str = 'Body response:\n\t- type: {}\n\t- content: {}'
    print(response_str.format(type(text), text))
