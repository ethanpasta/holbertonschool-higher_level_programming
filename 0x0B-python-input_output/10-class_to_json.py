#!/usr/bin/python3
import json

def class_to_json(obj):
    j = json.dumps(obj.__dict__)
    return j
