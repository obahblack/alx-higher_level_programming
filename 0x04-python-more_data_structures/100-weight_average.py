#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_product_sum = 0
    weight_sum = 0

    for score, weight in my_list:
        score_product_sum += score * weight
        weight_sum += weight

    return score_product_sum / weight_sum
