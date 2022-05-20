#!/usr/bin/python3
"""akes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get('https://api.github.com/user',
                        auth=(sys.argv[1], sys.argv[2]))
    print(resp.json().get("id"))
