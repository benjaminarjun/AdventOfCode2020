import unittest
from parameterized import parameterized
from .results import get_num_trees_hit


class TestTrajectoryAnalysis(unittest.TestCase):
    @parameterized.expand([
        [(1, 1), 2],
        [(3, 1), 7],
        [(5, 1), 3],
        [(7, 1), 4],
        [(1, 2), 2],
    ])
    def test_examples(self, slope, num_trees_hit):
        test_map = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ]

        actual = get_num_trees_hit(test_map, slope=slope)
        self.assertEqual(num_trees_hit, actual)
