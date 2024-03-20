#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    index = new_list.index(search)
    new_list[index] = replace

    return new_list
