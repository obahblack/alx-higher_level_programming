#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for stir in set_1:
        if stir in set_2:
            common.add(stir)
    return common
