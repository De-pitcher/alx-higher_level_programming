#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0 
    try:
        while count < x:
            try:
                print("{:d}".format(my_list[index]), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            index += 1
    except IndexError:
        raise
    finally:
        print("")
    return count
