#!/usr/bin/python3
import json

def load_from_json_file(filename):
    with open(filename) as f:
        obj = json.loads(f.read())
        return obj
