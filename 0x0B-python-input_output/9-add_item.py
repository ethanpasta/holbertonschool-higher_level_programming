#!/usr/bin/python3
import sys
import json
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


my_l = []
my_file = 'add_item.json'

if os.path.exists(my_file) and os.path.getsize(my_file) > 0:
    my_l = load_from_json_file(my_file)
for arg in sys.argv[1:]:
    my_l.append(arg)
save_to_json_file(my_l, "add_item.json")
