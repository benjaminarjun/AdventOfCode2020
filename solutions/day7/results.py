import re
from ..aoc_util import get_data


def parse_bag_container_requirements(req_lines):
    reqs = {}

    line_ptn = re.compile('(.*) bags contain (.*)\.')
    bag_list_ptn = re.compile('((\d+) (.*)|no other) bags?')

    for line in req_lines:
        line_match = re.match(line_ptn, line)
        contained_bags_str = line_match.group(2)

        if line_match.group(2) == 'no other bags':
            reqs[line_match.group(1)] = []
            continue

        contained_bags = []
        for bag_str in contained_bags_str.split(', '):
            bag_match = re.match(bag_list_ptn, bag_str)

            contained_bags.append((int(bag_match.group(2)), bag_match.group(3)))

        reqs[line_match.group(1)] = contained_bags

    return reqs


def get_valid_supercontainers(color, bag_container_reqs):
    traversed_nodes = []
    req_colors = {k: [z[1] for z in v] for k, v in bag_container_reqs.items()}
    these_containers = [k for k, v in req_colors.items() if color in v]

    while len(these_containers) > 0:
        traversed_nodes.extend(these_containers)
        these_containers = [
            k for k, v in req_colors.items() \
            if any([z for z in these_containers if z in v])
            and k not in traversed_nodes
        ]

    return set(traversed_nodes)


def get_num_bags_inside(color, bag_container_reqs):
    num_bags = 0

    if bag_container_reqs[color] == []:
        return 0

    for bag in bag_container_reqs[color]:
        num_bags += bag[0] * (get_num_bags_inside(bag[1], bag_container_reqs) + 1)

    return num_bags


if __name__ == '__main__':
    data = get_data(7, entry_trans=str)
    bag_container_reqs = parse_bag_container_requirements(data)
    print(f'Part 1:  {len(get_valid_supercontainers("shiny gold", bag_container_reqs))}')

    print(f'Part 2:  {get_num_bags_inside("shiny gold", bag_container_reqs)}')
