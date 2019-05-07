#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for j in row:
            print("{:d}".format(j), end='')
            if i != len(row) - 1:
                print(" ", end='')
            i = i + 1
        print("")
