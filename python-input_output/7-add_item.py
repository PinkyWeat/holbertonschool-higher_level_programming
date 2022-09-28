#!/usr/bin/python3
"""Module"""

import sys
"""sys module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    theList = []
    fileInQuestion = 'add_item.json'
    try:
        theList = load_from_json_file(fileInQuestion)
    except Exception:
        pass
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            theList.append(arg)
        save_to_json_file(theList, fileInQuestion)
