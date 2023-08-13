#!/usr/bin/python3
def no_c(my_string):
    new_string = [x in my_string if x != 'C' and x != 'c']
    return ("".join(new_string))
