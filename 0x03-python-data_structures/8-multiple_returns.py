#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) <= 0:
        first_chr = None
    else:
        first_chr = sentence[0]
    return (length, first_chr)
