from functools import reduce
from operator import mul

import itertools
import os


def get_data(day):
    path = os.path.join('..', '..', 'data', f'day{day}.txt')
    return open(path, 'r')


def parse_file_contents(raw_content):
    return [int(z.strip()) for z in raw_content.split('\n')]


def sum_finder(num_list, num_factors=2):
    in_data = [num_list for _ in range(num_factors)]
    options = list(itertools.product(*in_data))

    for option in options:
        if sum(option) == 2020:
            return option

    return None


if __name__ == '__main__':
    with get_data(1) as f:
        num_list = parse_file_contents(f.read())
        nums = sum_finder(num_list)
        print(f'Part 1: {reduce(mul, nums)}')

        nums = sum_finder(num_list, num_factors=3)
        print(f'Part 2: {reduce(mul, nums)}')

