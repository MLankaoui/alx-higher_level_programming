#!/usr/bin/python3
for o in range(0, 9):
    for i in range(1, 10):
        if o == 8 and i == 9:
            end = "\n"
        else:
            end = ", "
        if o < i:
            print("{o}{i}".format(o=o, i=i), end=end)
