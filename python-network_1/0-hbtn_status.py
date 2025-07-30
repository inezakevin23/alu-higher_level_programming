#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    '\n    AppleWebKit/537.36 (KHTML, like Gecko)'
    '\n    Chrome/99.0.4844.84 Safari/537.36',
}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))

