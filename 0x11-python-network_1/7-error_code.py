#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL,
    and displays the body of the response.
"""
import sys
import requests
""" sys imports the arguments passed to the script
    urllib imports the requests module
"""

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
