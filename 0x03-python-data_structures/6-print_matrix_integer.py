#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        ll = 1
        for j in i:
            if ll == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            ll += 1
        print()
