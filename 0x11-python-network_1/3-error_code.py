#!/usr/bin/python3
"""Takes a URL sends a request to URL and displays
body of response (decoded in utf-8)."""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as Error:
        print("Error code: {}".format(Error.code))
