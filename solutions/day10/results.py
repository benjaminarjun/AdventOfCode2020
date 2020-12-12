from ..aoc_util import get_data


def get_joltage_diff_dist(adapter_ratings):
    diffs_ret = {1: 0, 2: 0, 3: 0}
    ratings = _get_padded_adapter_ratings(adapter_ratings)

    diffs = [x - y for x, y in zip(ratings[1:], ratings)]
    diffs_ret.update({num: len([z for z in diffs if z == num]) for num in set(diffs)})

    return diffs_ret


def get_num_arrangements(adapter_ratings):
    ratings = _get_padded_adapter_ratings(adapter_ratings)
    last_adapter = max(ratings)

    return _get_num_paths_leading_to(last_adapter, ratings)


def _get_num_paths_leading_to(n, adapter_ratings, calculated_vals=None):
    calculated_vals = {} if calculated_vals is None else calculated_vals

    # return from the cache if present
    if n in calculated_vals:
        retval = calculated_vals[n]
        # return 1 if it's the first node in the chain
    elif n == min(adapter_ratings):
        retval = 1
    else:
        # otherwise, get an answer for this number (and cache before returning)
        path_sums = []

        for j in range(n - 3, n):
            if j not in adapter_ratings:
                continue

            num_paths_to_j = _get_num_paths_leading_to(j, adapter_ratings, calculated_vals)
            path_sums.append(num_paths_to_j)

        retval = sum(path_sums)

    calculated_vals[n] = retval
    return retval


def _get_padded_adapter_ratings(ratings):
    # Add rating of initial and final device
    r = ratings.copy()
    r.extend([0, max(ratings) + 3])
    return sorted(r)


if __name__ == '__main__':
    data = get_data(10, entry_trans=int)
    joltage_diffs = get_joltage_diff_dist(data)

    print(f'Part 1:  {joltage_diffs[1] * joltage_diffs[3]}')

    print(f'Part 2:  {get_num_arrangements(data)}')
