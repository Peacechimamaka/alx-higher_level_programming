#!/bin/bash
# Takes in a URL, sends request to it and displays the body-size of the response

curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
