#!/bin/bash
#script that takes in a URL, sends a POST request to the passed URL,and displays the body of the response
curl -sX POST $1 -d "emial=test@gmail.com&subject=I will always be here for PLD" -L
