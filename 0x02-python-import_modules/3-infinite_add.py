#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1

    result = 0

    i = 1

    if argc == 0:
        print("0")

    elif argc > 0:
        for number in sys.argv[1:]:
            result += int(sys.argv[i])
            i += 1

        print(result)
