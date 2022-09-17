#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    res = 0
    for elem in my_list:
        found = False
        for addelem in uniq:
            if elem is addelem:
                found = True
        if found is False:
            uniq.append(elem)
            res += elem
    return res