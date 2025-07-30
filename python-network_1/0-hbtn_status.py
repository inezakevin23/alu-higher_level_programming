#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status using urllib and print the body."""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print(content.decode('utf-8'))

