#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
