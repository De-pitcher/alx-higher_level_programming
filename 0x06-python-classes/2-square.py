#!/usr/bin/python3
'''Define Square class'''


class Square:
    '''Represent the Square class'''
    def __init__(self, size):
    '''Initialize a new class

    Args:
        size (int): The size of the new square.
    '''
    if not isinstance(szie, int):
        rreaise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be += 0")
    self.__size = size
