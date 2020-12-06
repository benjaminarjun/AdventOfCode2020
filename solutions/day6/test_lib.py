import unittest
from .results import get_answers_per_group


class TestCustomsFormReader(unittest.TestCase):
    def test_get_answers_per_group(self):
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

        lines = [z.strip() for z in document.split('\n')]

        expected = [
            set(['a', 'b', 'c']),
            set(['a', 'b', 'c']),
            set(['a', 'b', 'c']),
            set(['a']),
            set(['b']),
        ]

        self.assertEqual(expected, get_answers_per_group(lines))
