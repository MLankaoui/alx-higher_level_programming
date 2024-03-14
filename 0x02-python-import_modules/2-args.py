import sys

argc = len(sys.argv)

i = 0
if argc == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv))

elif argc > 2:
    print("{} arguments:".format(argc))

    for argument in sys.argv:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

else:
    print(".")

