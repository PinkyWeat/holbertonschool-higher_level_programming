#!/usr/bin/python3
from hashlib import new


def new_in_list(my_list, idx, element):
    if idx < 0 or idx not in range(0, len(my_list)) or my_list is None:
        return my_list
    else:
        new_list = list(my_list)
        new_list[idx] = element
        return new_list