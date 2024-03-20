#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    if search in new_list:
        index = new_list.index(search)
        new_list[index] = replace
    else:
        new_list.append(search)

    return new_list
