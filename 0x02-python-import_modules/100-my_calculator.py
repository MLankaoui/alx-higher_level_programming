#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, add, div, mul

    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

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
