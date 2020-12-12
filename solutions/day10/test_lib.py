import unittest
from .results import get_joltage_diff_dist


class TestAdapterLinkingFinder(unittest.TestCase):
    @property
    def data_ex_1(self):
        return [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4,
        ]

    @property
    def data_ex_2(self):
        return [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]

    def test_joltage_linking_ex_1(self):
        adapter_ratings = self.data_ex_1

        expected = {1: 7, 2: 0, 3: 5}

        self.assertEqual(expected, get_joltage_diff_dist(adapter_ratings))

    def test_joltage_linking_ex_2(self):
        adapter_ratings = self.data_ex_2

        expected = {1: 22, 2: 0, 3: 10}

        self.assertEqual(expected, get_joltage_diff_dist(adapter_ratings))
