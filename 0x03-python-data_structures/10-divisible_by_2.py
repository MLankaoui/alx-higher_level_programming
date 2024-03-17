#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for element in my_list:
        if element % 2 == 0:
            new_list.append(element)
            return True
        else:
            return False
    return new_list