#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    my_tuple = (sentence_length, sentence[0])
    if len(sentence) == 0:
        sentence_length = 0
        sentence[0] = None
        return my_tuple
    else:
        return my_tuple
