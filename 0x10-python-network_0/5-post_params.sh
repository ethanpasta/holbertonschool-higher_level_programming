#!/bin/bash
# Script sends a post request with data
curl --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" -s $1
