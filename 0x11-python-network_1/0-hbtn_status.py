#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        respnse = response.read()

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(respnse), respnse, respnse.decode('utf-8')))
