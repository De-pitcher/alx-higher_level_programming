#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    index = int_counts = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end="")
                index += 1
                int_counts += 1
            else:
                print()
                return int_counts
        except (ValueError, TypeError):
            index += 1
