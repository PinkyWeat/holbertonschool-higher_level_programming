#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        theTuple = (0, 0)
        return theTuple
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        theTuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return theTuple
    elif len(tuple_b) == 1 and len(tuple_a) == 2:
        theTuple = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return theTuple
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        theTuple = (tuple_a[0] + tuple_b[0])
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        theTuple = tuple_b
        return theTuple
    elif len(tuple_b) == 0 and len(tuple_a) == 2:
        return tuple_a
    theTuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return theTuple
