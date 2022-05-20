#!/usr/bin/python3
"""Takes a URL sends a request to URL and displays
body of response"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    if requests.get(url).status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(request.get(url).text)
