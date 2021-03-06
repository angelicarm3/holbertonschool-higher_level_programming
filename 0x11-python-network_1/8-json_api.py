#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]

    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        resp_json = resp.json()
        if resp_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp_json.get("id"), resp_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
