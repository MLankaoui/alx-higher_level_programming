#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    length = len(my_list)
    for element in range(length - 1, -1, -1):
        print("{}".format(my_list[element]))
