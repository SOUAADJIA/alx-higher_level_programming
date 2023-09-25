#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    element = 0
    for val in my_list:
        try:
            if element >= x:
                break
            print('{:d}'.format(val), end='')
            element = element + 1
        except (ValueError, TypeError):
            continue
    print()
    return element
