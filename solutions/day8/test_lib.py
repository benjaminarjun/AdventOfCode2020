import unittest
from .results import BootCodeComputer, ComputerState


class TestBootCodeComputer(unittest.TestCase):
    def test_boot_code_computer(self):
        instruction_strs = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6',
        ]

        computer = BootCodeComputer(instruction_strs)
        self.assertEqual(ComputerState.New, computer.state)

        computer.run_until_repeat()
        self.assertEqual(ComputerState.Paused, computer.state)

        expected = 5
        actual = computer.accumulator

        self.assertEqual(expected, actual)
