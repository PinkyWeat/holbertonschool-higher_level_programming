#!/usr/bin/python3
"""Module"""
import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fileInQuestion = 'add_item.json'
theList = []

if os.path.exists(fileInQuestion) and os.path.getsize(fileInQuestion) > 0:
    theList = load_from_json_file(fileInQuestion)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        theList.append(arg)

save_to_json_file(theList, fileInQuestion)
