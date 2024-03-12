#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        end = ", "
    else:
        end = "\n"
    if number < 10:
        print("0{number}".format(number=number), end=end)
    else:
        print("{number}".format(number=number), end=end)
