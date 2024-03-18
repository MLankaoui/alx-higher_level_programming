#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = (len(sentence), sentence[0])
    if len(sentence) == 0:
        sentence[0] = None
        return my_tuple
    else:
        return my_tuple
