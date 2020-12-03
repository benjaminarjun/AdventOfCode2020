import unittest
from results import parse_file_contents, sum_finder


class TestSumFinder(unittest.TestCase):    
    def test_parse_file_contents(self):
        document = """1
2
3"""
        contents = parse_file_contents(document)
        self.assertEqual([1, 2, 3], contents)

    def test_sum_finder_example(self):
        in_data = [1721, 979, 366, 299, 675, 1456]
        expected = (1721, 299)
        actual = sum_finder(in_data)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
