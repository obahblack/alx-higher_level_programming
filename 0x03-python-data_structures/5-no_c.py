#!/usr/bin/python3
def no_c(my_string):
    str_1 = ""
    for char in my_string:
        if char != "c" and char != "C":
            str_1 = str_1 + char
    return str_1
