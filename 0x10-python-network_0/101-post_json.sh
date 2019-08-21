#!/bin/bash
# Script sends a JSON post request
curl -sX "POST" "$1" -d @"$2" --header "Content-Type: application/json"
