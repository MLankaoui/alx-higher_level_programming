#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):

        if number % 3 != 0 and number % 5 != 0:
            print("{number} ".format(number=number), end="")

        else:
            if number % 3 == 0:
                print("Fizz ", end="")
                number += 1
            elif number % 5 == 0:
                print("Buzz ", end="")
                number += 1
            elif number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz ", end="")
                number += 1
