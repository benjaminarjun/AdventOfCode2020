from ..aoc_util import get_data
import itertools


LENGTH_CHAR_MAPPING = {'F': 0, 'B': 1}
WIDTH_CHAR_MAPPING = {'L': 0, 'R': 1}


def _get_plane_dim_powers(boarding_pass):
    sep_ix = min([i for i, z in enumerate(boarding_pass) if z not in LENGTH_CHAR_MAPPING.keys()])
    return sep_ix, len(boarding_pass) - sep_ix


def _get_dim_pos(sub_instruction, val_map):
    initial_size = 2 ** len(sub_instruction)
    current_pos = 0
    next_partition_size = initial_size // 2

    for char in sub_instruction:
        if val_map[char] == 1:
            current_pos += next_partition_size

        next_partition_size = next_partition_size // 2

    return current_pos


def get_seat(boarding_pass):
    # get dimensions of plane as implied by instruction
    dims = _get_plane_dim_powers(boarding_pass)
    length_instr, width_instr = boarding_pass[:dims[0]], boarding_pass[dims[0]:]

    # ensure each substring of the instruction is valid
    # need only check width because the above logic already took the largest valid length sub-instruction
    if any([z not in WIDTH_CHAR_MAPPING.keys() for z in width_instr]):
        raise ValueError('Invalid `instruction` supplied')

    # perform partitioning on each dimension
    length_pos = _get_dim_pos(length_instr, LENGTH_CHAR_MAPPING)
    width_pos = _get_dim_pos(width_instr, WIDTH_CHAR_MAPPING)

    return length_pos, width_pos


def get_seat_id(seat):
    return 8 * seat[0] + seat[1]


def find_open_seats(boarding_passes):
    example_bp = boarding_passes[0]
    dims = tuple(2 ** z for z in _get_plane_dim_powers(example_bp))

    all_seats = [seat for seat in itertools.product(range(dims[0]), range(dims[1]))]
    boarding_pass_seat_ids = [get_seat_id(get_seat(bp)) for bp in boarding_passes]

    return [seat for seat in all_seats if get_seat_id(seat) not in boarding_pass_seat_ids]


if __name__ == '__main__':
    boarding_passes = get_data(5, entry_trans=str)
    max_seat_id = max([get_seat_id(get_seat(bp)) for bp in boarding_passes])

    print(f'Part 1:  {max_seat_id}')

    open_seats = find_open_seats(boarding_passes)
    bp_ids = [get_seat_id(get_seat(bp)) for bp in boarding_passes]

    my_seat_possibilities = []
    for seat in open_seats:
        seat_id = get_seat_id(seat)
        if seat_id + 1 in bp_ids and seat_id - 1 in bp_ids:
            my_seat_possibilities.append(seat)

    if len(my_seat_possibilities) != 1:
        raise Exception('Did not find a unique solution; something is wrong')
    else:
        my_seat_id = get_seat_id(my_seat_possibilities[0])
        print(f'Part 2:  {my_seat_id}')
