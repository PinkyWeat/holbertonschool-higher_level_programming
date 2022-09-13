#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'c':
            my_string = my_string.replace('c', '')
        if i == 'C':
            my_string = my_string.replace('C', '')
    return my_string
