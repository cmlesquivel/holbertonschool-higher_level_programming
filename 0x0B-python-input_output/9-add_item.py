#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

my_list = []
list_import = []
filename = "add_item.json"

if len(sys.argv) > 1:
    my_list = sys.argv[1:]
try:
    list_import = load_from_json_file(filename)
except:
    pass

list_export = list_import + my_list

save_to_json_file(list_export, filename)
