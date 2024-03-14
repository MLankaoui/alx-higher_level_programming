import sys

argc = len(sys.argv) - 1

i = 1
if argc == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))

elif argc > 1:
    print("{} arguments:".format(argc))

    for argument in sys.argv[1:]:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

else:
    print(".")

