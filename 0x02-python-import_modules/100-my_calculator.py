#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, add, div, mul

    argc = len(sys.argv) - 1

    result = 0

    operator = ""

    if argc < 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(sys.argv[1],sys.argv[2], sys.argv[3], add(int(sys.argv[1]), int(sys.argv[3]))))

        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(sys.argv[1],sys.argv[2], sys.argv[3], sub(int(sys.argv[1]), int(sys.argv[3]))))
        
        elif sys.argv[2] == '/':
            print("{} {} {} = {}".format(sys.argv[1],sys.argv[2], sys.argv[3], div(int(sys.argv[1]), int(sys.argv[3]))))

        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(sys.argv[1],sys.argv[2], sys.argv[3], mul(int(sys.argv[1]), int(sys.argv[3]))))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    