#!/bin/bash
# Script that takes in a URL and displays the size of the body of the response in bytes

curl -s "$1" | wc -c
