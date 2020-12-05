import unittest
from ..aoc_util import parse_file_contents


class TestAocUtil(unittest.TestCase):
    def test_parse_file_contents(self):
        document = """1
2
3"""
        int_contents = parse_file_contents(document, entry_trans=int)
        self.assertEqual([1, 2, 3], int_contents)

        str_contents = parse_file_contents(document, entry_trans=str)
        self.assertEqual(['1', '2', '3'], str_contents)
