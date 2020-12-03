import unittest
from .results import Password


class TestPasswordParser(unittest.TestCase):
    def test_part_1_example(self):
        pws = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        expected = [True, False, True]

        for pw, exp in zip(pws, expected):
            self.assertEqual(exp, Password(pw).is_valid_sled_pw())

    def test_part_2_example(self):
        pws = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        expected = [True, False, False]

        for pw, exp in zip(pws, expected):
            self.assertEqual(exp, Password(pw).is_valid_toboggan_pw())
