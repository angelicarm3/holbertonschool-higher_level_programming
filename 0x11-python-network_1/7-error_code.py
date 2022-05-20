#!/usr/bin/python3
"""Takes a URL sends a request to URL and displays
body of response"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    resp = requests.get(url)

    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
