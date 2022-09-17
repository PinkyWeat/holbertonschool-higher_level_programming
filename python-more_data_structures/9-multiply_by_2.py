#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for pages in new_dictionary.keys():
        new_dictionary[pages] *= new_dictionary[pages]
    return new_dictionary
