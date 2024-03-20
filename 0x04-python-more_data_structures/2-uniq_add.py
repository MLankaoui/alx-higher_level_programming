#!/usr/bin/python3
def uniq_add(my_list=[]):
    results = 0
    new_set = list(set(my_list))
    for element in new_set:
        results += element

    return results
