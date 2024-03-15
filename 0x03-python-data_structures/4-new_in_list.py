#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original_list = []
    new_list = []

    if idx < 0 and idx > len(my_list) - 1:
        original_list = my_list
        return original_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
