from ..aoc_util import get_data


def get_joltage_diff_dist(adapter_ratings):
    diffs_ret = {1: 0, 2: 0, 3: 0}
    ratings = adapter_ratings.copy()

    # Add rating of initial and final device
    ratings.extend([0, max(ratings) + 3])
    ratings.sort()

    diffs = [x - y for x, y in zip(ratings[1:], ratings)]
    diffs_ret.update({num: len([z for z in diffs if z == num]) for num in set(diffs)})

    return diffs_ret


if __name__ == '__main__':
    data = get_data(10, entry_trans=int)
    joltage_diffs = get_joltage_diff_dist(data)

    print(f'Part 1:  {joltage_diffs[1] * joltage_diffs[3]}')

    print(f'Part 2:  NOT IMPLEMENTED')
