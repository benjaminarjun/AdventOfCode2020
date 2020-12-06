from ..aoc_util import get_data


def _parse_document(document):
    group_entries = []

    group_entry = []
    for line in document:
        if line == '':
            group_entries.append(group_entry)
            group_entry = []
        else:
            if group_entry == []:
                group_entry = [line]
            else:
                group_entry.append(line)

    # Add any leftovers as a full group entry
    if group_entry != []:
        group_entries.append(group_entry)

    return [[set(k) for k in g] for g in group_entries]


def get_group_answer_unions(document):
    group_entries = _parse_document(document)
    return [set.union(*g) for g in group_entries]


def get_group_answer_intersections(document):
    group_entries = _parse_document(document)
    return [set.intersection(*g) for g in group_entries]


if __name__ == '__main__':
    data = get_data(6, entry_trans=str)

    group_answer_unions = get_group_answer_unions(data)
    print(f'Part 1:  {sum([len(z) for z in group_answer_unions])}')

    group_answer_intersections = get_group_answer_intersections(data)
    print(f'Part 2:  {sum([len(z) for z in group_answer_intersections])}')
