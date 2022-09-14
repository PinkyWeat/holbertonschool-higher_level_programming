#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        i = 0
        for val in row:
            print("{:d}".format(val), end=" " if i < len(row) - 1 else "\n")
            i += 1
