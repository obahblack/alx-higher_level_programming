#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in range(0, len(matrix)):
        sq = list(map(lambda x: x**2, matrix[i]))
        new_matrix.append(sq)
    return (new_matrix)
