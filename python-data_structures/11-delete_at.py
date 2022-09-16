##!/usr/bin/python3
from dataclasses import replace
from os import remove


def delete_at(my_list=[], idx=0):
    if my_list == 0:
        return None
    if idx < 0 or not range(0, len(my_list)):
        return my_list
    else:
        del my_list[idx]
        return my_list
