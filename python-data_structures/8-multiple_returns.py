#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        sentence[0] = None
        return sentence[0]
    theTuple = (len(sentence), sentence[0])
    return theTuple
