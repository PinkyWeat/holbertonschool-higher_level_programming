#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for elem in set_1:
        for elem2 in set_2:
            addE = False
            for other_elem in common:
                if other_elem is elem2:
                    addE = True
            # compares elems and
            if elem is elem2 and addE is False:
                common.append(elem2)
    return common
