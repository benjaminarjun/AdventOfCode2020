import unittest
from .results import XmasCypher


class TestXmasCypher(unittest.TestCase):
    @property
    def data(self):
        return [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ]

    def test_detect_invalid_numbers(self):
        cypher = XmasCypher(self.data, preamble_len=5)
        while cypher.index < len(cypher.data):
            if cypher.current_val == 127:
                self.assertFalse(cypher.check_next())
            else:
                self.assertTrue(cypher.check_next())

    def test_find_contiguous_sublist_summing_to(self):
        cypher = XmasCypher(self.data, preamble_len=5)
        expected = [15, 25, 47, 40]
        actual = cypher.find_contiguous_sublist_summing_to(127)

        self.assertEqual(expected, actual)
