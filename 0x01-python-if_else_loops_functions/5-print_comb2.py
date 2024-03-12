#!/usr/bin/python3
for deci in range(0, 10):
    for units in range(0, 10):
        if deci != 9 or units != 9:
            print("{deci}{units}, ".format(deci=deci, units=units), end="")
        elif deci == 9 and units == 9:
            print("{deci}{units}".format(deci=deci, units=units))
