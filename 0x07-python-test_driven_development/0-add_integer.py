#!/usr/bin/python3
def add_integer(a, b=98):
    """Add integer"""
    if a not in range(0, 10):
        raise TypeError("a must be in integer")
    if b not in range(0, 10):
        raise TypeError("b must be in integer")
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("/test/0-add_integer.txt")