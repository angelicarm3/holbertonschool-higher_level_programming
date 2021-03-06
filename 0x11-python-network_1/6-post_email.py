#!/usr/bin/python3
"""Takes a URL and an email sends POST request to the URL with
email as parameter and displays the body of the response"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    resp = requests.post(url, data=value)
    print(resp.text)
