#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        sentence[0] = None
    theTuple = (len(sentence), sentence[0])
    return theTuple
