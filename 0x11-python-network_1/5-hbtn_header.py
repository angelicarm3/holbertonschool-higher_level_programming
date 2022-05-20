#!/usr/bin/python3
"""Takes a URL, sends request to URL and displays
value of X-Request-Id in response header"""


if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]

    resp = requests.get(url)
    print(resp.headers.get("X-Request-Id"))
