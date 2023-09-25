#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    element = 0
    try:
        for val in my_list:
            if element >= x:
                break
            if isinstance(val, int):
                print('{:d}'.format(val), end='')
                element = element + 1
    except (ValueError, TypeError):
        pass

    print()
    return element
