from functools import reduce
from operator import mul
from ..aoc_util import get_data

import itertools
import os


def sum_finder(num_list, num_factors=2):
    in_data = [num_list for _ in range(num_factors)]
    options = list(itertools.product(*in_data))

    for option in options:
        if sum(option) == 2020:
            return option

    return None


if __name__ == '__main__':
    num_list = get_data(1)
    nums = sum_finder(num_list)
    print(f'Part 1: {reduce(mul, nums)}')

    nums = sum_finder(num_list, num_factors=3)
    print(f'Part 2: {reduce(mul, nums)}')

