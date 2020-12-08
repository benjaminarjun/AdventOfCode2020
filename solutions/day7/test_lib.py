import unittest
from .results import parse_bag_container_requirements, get_valid_supercontainers, \
    get_num_bags_inside


class TestBagColorRules(unittest.TestCase):
    @property
    def data(self):
        return [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
            'bright white bags contain 1 shiny gold bag.',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
            'faded blue bags contain no other bags.',
            'dotted black bags contain no other bags.',
        ]

    def test_parse_bag_container_requirements(self):
        expected = {
            'light red': [(1, 'bright white'), (2, 'muted yellow')],
            'dark orange': [(3, 'bright white'), (4, 'muted yellow')],
            'bright white': [(1, 'shiny gold')],
            'muted yellow': [(2, 'shiny gold'), (9, 'faded blue')],
            'shiny gold': [(1, 'dark olive'), (2, 'vibrant plum')],
            'dark olive': [(3, 'faded blue'), (4, 'dotted black')],
            'vibrant plum': [(5, 'faded blue'), (6, 'dotted black')],
            'faded blue': [],
            'dotted black': [],
        }

        self.assertEqual(expected, parse_bag_container_requirements(self.data))

    def test_get_valid_supercontainers(self):
        bag_container_reqs = parse_bag_container_requirements(self.data)
        expected = set(['bright white', 'muted yellow', 'dark orange', 'light red'])
        actual = get_valid_supercontainers('shiny gold', bag_container_reqs)

        self.assertEqual(expected, actual)

    def test_get_num_bags_inside(self):
        reqs_list = [
            'shiny gold bags contain 2 dark red bags.',
            'dark red bags contain 2 dark orange bags.',
            'dark orange bags contain 2 dark yellow bags.',
            'dark yellow bags contain 2 dark green bags.',
            'dark green bags contain 2 dark blue bags.',
            'dark blue bags contain 2 dark violet bags.',
            'dark violet bags contain no other bags.',
        ]

        reqs = parse_bag_container_requirements(reqs_list)
        self.assertEqual(126, get_num_bags_inside('shiny gold', reqs))
