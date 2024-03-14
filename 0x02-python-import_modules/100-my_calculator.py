#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, add, div, mul

    argc = len(sys.argv) - 1

    result = 0

    operator = ""

    a = int(sys.argv[1])

    b = int(sys.argv[3])

    operator = sys.argv[2]

    if argc < 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))

        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))

        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
