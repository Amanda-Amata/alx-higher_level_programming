#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL,
    and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.requests
import urllib.error
""" sys imports arguments passed to the script
    urllib imports error and request modules
"""
if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
