from ..aoc_util import get_data


def _get_dim(sub_instruction, val_map):
    initial_size = 2 ** len(sub_instruction)
    current_pos = 0
    next_partition_size = initial_size // 2

    for char in sub_instruction:
        if val_map[char] == 1:
            current_pos += next_partition_size

        next_partition_size = next_partition_size // 2

    return current_pos


def get_seat(instruction):
    length_char_mapping = {'F': 0, 'B': 1}
    width_char_mapping = {'L': 0, 'R': 1}

    # get dimensions of plane as implied by instruction
    sep_ix = min([i for i, z in enumerate(instruction) if z not in length_char_mapping.keys()])
    length_instr, width_instr = instruction[:sep_ix], instruction[sep_ix:]

    # ensure each substring of the instruction is valid
    # need only check width because the above logic already took the largest valid length sub-instruction
    if any([z not in width_char_mapping.keys() for z in width_instr]):
        raise ValueError('Invalid `instruction` supplied')

    # perform partitioning on each dimension
    length_pos = _get_dim(length_instr, length_char_mapping)
    width_pos = _get_dim(width_instr, width_char_mapping)

    return length_pos, width_pos


def get_seat_id(seat):
    return 8 * seat[0] + seat[1]


if __name__ == '__main__':
    boarding_passes = get_data(5, entry_trans=str)
    max_seat_id = max([get_seat_id(get_seat(bp)) for bp in boarding_passes])

    print(f'Part 1:  {max_seat_id}')

    print(f'Part 2:  NOT IMPLEMENTED')
