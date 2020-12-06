import unittest
from .results import get_group_answer_unions, get_group_answer_intersections


class TestCustomsFormReader(unittest.TestCase):
    @property
    def data(self):
        document = """abc

a
b
c

ab
ac

a
a
a
a

b"""

        return [z.strip() for z in document.split('\n')]

    def test_get_group_answer_unions(self):
        expected = [
            set(['a', 'b', 'c']),
            set(['a', 'b', 'c']),
            set(['a', 'b', 'c']),
            set(['a']),
            set(['b']),
        ]

        self.assertEqual(expected, get_group_answer_unions(self.data))

    def test_get_group_answer_intersections(self):
        expected = [
            set(['a', 'b', 'c']),
            set([]),
            set(['a']),
            set(['a']),
            set(['b']),
        ]

        self.assertEqual(expected, get_group_answer_intersections(self.data))
