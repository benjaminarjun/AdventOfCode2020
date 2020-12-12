import unittest
import pathlib
from parameterized import parameterized
from .results import Grid, TerminalSeating


def _load_data(file_name):
    full_path = pathlib.Path(__file__).parent.joinpath('test_vals', file_name)

    with open(full_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


class TestGrid(unittest.TestCase):
    def test_get(self):
        grid = Grid(['as', 'df'])
        coord = (1, 0)
        self.assertEqual('d', grid.get_val(coord))

    def test_set(self):
        grid = Grid(['as', 'df'])
        coord = (1, 0)
        grid.set_val(coord, 'g')

        self.assertEqual('g', grid.get_val(coord))


class TestTerminalSeating(unittest.TestCase):
    def test_ex_1_setup(self):
        initial = _load_data('initial.txt')
        seating = TerminalSeating(initial)

        self.assertEqual(Grid(initial), seating.initial)
        self.assertEqual(Grid(initial), seating.current)
        self.assertEqual(0, seating.epoch)


    @parameterized.expand([
        [_load_data('expected_epoch_1.txt'), 1],
        [_load_data('expected_epoch_2.txt'), 2],
        [_load_data('expected_epoch_3.txt'), 3],
        [_load_data('expected_epoch_4.txt'), 4],
        [_load_data('expected_epoch_5.txt'), 5],
    ])
    def test_ex_1_state_after_num_epochs(self, expected, num_epochs):
        initial = _load_data('initial.txt')
        seating = TerminalSeating(initial)
        seating.run_epochs(num_epochs)

        self.assertEqual(expected, seating.current)

    def test_equilibrium_finder(self):
        initial = _load_data('initial.txt')
        seating = TerminalSeating(initial)

        seating.run_until_equilibrium()
        self.assertEqual(6, seating.equilibrium_epoch)
