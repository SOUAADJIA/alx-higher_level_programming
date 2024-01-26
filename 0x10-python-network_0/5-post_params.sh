#!/bin/bash
# This script sends a POST request to the URL with custom parameters and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
