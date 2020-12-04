"""Add an empty data file and a new folder with standard files"""

import os
import sys


if len(sys.argv) != 2:
    raise Exception('Expected exactly one numeric argument representing day to scaffold')

day = int(sys.argv[1])


# create empty file for data
data_path = os.path.join('data', f'day{day}.txt')
with open(data_path, 'w'):
    pass


# create new folder for solution
day_dir = os.path.join('solutions', f'day{day}')
os.mkdir(day_dir)


# create standard solution folder contents
init_path = os.path.join(day_dir, '__init__.py')
results_path = os.path.join(day_dir, 'results.py')
test_path = os.path.join(day_dir, 'test_lib.py')

results_contents = """from ..aoc_util import get_data


if __name__ == '__main__':
    print(f'Part 1:  NOT IMPLEMENTED')

    print(f'Part 2:  NOT IMPLEMENTED')
"""

test_contents = f"""import unittest


class TestDay{day}(unittest.TestCase):
    def test_fail(self):
        self.assertTrue(False)
"""

with open(init_path, 'w') as f:
    pass

with open(results_path, 'w') as f:
    f.write(results_contents)

with open(test_path, 'w') as f:
    f.write(test_contents)
