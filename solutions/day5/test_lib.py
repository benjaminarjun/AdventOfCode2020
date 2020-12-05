from parameterized import parameterized
import unittest
from .results import get_seat, get_seat_id


class TestBinarySpacePartitioner(unittest.TestCase):
    def test_get_seat_raises_on_invalid_instruction(self):
        with self.assertRaises(ValueError):
            get_seat('asdf')

    @parameterized.expand([
        ['FBFBBFFRLR', (44, 5)],
        ['BFFFBBFRRR', (70, 7)],
        ['FFFBBBFRRR', (14, 7)],
        ['BBFFBBFRLL', (102, 4)],
    ])
    def test_get_seat_ex_1(self, instruction, expected):
        self.assertEqual(expected, get_seat(instruction))

    @parameterized.expand([
        [(44, 5), 357],
        [(70, 7), 567],
        [(14, 7), 119],
        [(102, 4), 820],
    ])
    def test_seat_id_examples(self, seat, expected):
        self.assertEqual(expected, get_seat_id(seat))
