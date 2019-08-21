#!/bin/bash
# Script sends a request, displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
