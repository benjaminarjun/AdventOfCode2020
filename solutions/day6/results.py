from ..aoc_util import get_data


def get_answers_per_group(document):
    group_entries = []

    group_entry = ''
    for line in document:
        if line == '':
            group_entries.append(group_entry)
            group_entry = ''
        else:
            if group_entry == '':
                group_entry = line
            else:
                group_entry += line

    # Add any leftovers as a full group entry
    if group_entry != '':
        group_entries.append(group_entry)

    return [set(g) for g in group_entries]


if __name__ == '__main__':
    data = get_data(6, entry_trans=str)
    answers_per_group = get_answers_per_group(data)


    print(f'Part 1:  {sum([len(z) for z in answers_per_group])}')

    print(f'Part 2:  NOT IMPLEMENTED')
