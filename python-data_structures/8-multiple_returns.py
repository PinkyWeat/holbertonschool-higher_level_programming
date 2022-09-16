#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None or sentence == "":
        sentence[0] = None
        return None
    theTuple = (len(sentence), sentence[0])
    return theTuple
