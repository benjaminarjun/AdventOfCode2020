from functools import reduce
from operator import mul
from ..aoc_util import get_data


def get_num_trees_hit(geog_map, slope):
    num_hits = 0
    mod_by = len(geog_map[0])

    pos = (0, 0)

    while pos[1] < len(geog_map):
        if geog_map[pos[1]][pos[0] % mod_by] == '#':
            num_hits += 1

        pos = tuple(sum(x) for x in zip(pos, slope))

    return num_hits


if __name__ == '__main__':
    data = get_data(3, entry_trans=str)
    num_trees_hit = get_num_trees_hit(data, slope=(3, 1))

    print(f'Part 1:  {num_trees_hit}')

    part_2_slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    tree_hits = [get_num_trees_hit(data, slope) for slope in part_2_slopes]
    tree_hits_mul = reduce(mul, tree_hits)

    print(f'Part 2:  {tree_hits_mul}')
