#!/usr/bin/python3
"""script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
"""
import sys
import requests
""" sys imports the arguments passed to the script
    urllib imports the request module
"""

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(ur, data=value)
    print(req.text)
