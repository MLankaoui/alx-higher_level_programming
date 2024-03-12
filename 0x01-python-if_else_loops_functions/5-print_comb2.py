#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        if number < 10:
            print("{:d}".format(0), end="")
        print("{number}, ".format(number=number), end="")

    else:
        number += 1
