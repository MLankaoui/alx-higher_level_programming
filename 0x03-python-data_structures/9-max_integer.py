#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    max_number = my_list[0]

    for element in my_list:
        if element > max_number:
            max_number = element

    return max_number
