#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_printed = 0

    for i in range(x):
        try:
            element_printed += 1
            print(my_list[i], end='')
        except IndexError:
            break

    print()
    return element_printed
