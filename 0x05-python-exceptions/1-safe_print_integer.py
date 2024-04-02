#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(value, end="")
        return (True)
    except TypeError:
        pass
        return (False)
    finally:
        print()