#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""
if __name__ == '__main__':
	import urllib.request

	url = 'https://alu-intranet.hbtn.io/status'
	headers = {
   	 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
   	 '\n    AppleWebKit/537.36 (KHTML, like Gecko)'
  	  '\n    Chrome/99.0.4844.84 Safari/537.36',
	}
	req = urllib.request.Request(url, headers=headers)

 	with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        	content = res.read()
        	print("Body response:")
        	print("\t- type: {}".format(type(content)))
        	print("\t- content: {}".format(content))
        	print("\t- utf8 content: {}".format(content.decode('utf-8')))
