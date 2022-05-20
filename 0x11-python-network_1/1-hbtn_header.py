#!/usr/bin/python3
"""takes a URL, sends a request to URL and displays value of X-Request-Id"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        answer = header.get("X-Request-Id")
    print(answer)
