"""Random function wrapper"""


import time
from random import randint, seed


def get_random_number(int_begin, int_end):
    """used in all games"""
    seed(time.clock())
    random_number = randint(int_begin, int_end)

    return random_number
