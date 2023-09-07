#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # without script name

    nbr_args = len(argv)

    if nbr_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(nbr_args, 's' if nbr_args != 1 else ''))

        position = 1
        for arg in argv:
            print("{}: {}".format(position, arg))
            position += 1
