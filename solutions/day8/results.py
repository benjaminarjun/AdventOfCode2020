from ..aoc_util import get_data
import collections
from enum import Enum
import re


class ComputerState(Enum):
    New = 1
    Paused = 2
    Terminated = 3


class BootCodeComputer:
    def __init__(self, instruction_strs):
        instr_ptn = re.compile('(nop|acc|jmp) ([+-]\d+)')
        Instruction = collections.namedtuple('Instruction', 'op arg')

        self.state = ComputerState.New
        self.accumulator = 0
        self.index = 0
        self._visited_indexes = []

        self.instructions = []
        for instruction_str in instruction_strs:
            match = re.match(instr_ptn, instruction_str)
            instruction = Instruction(op=match.group(1), arg=int(match.group(2)))
            self.instructions.append(instruction)

    def _add_to_index(self, val):
        self._visited_indexes.append(self.index)
        self.index += val

    def run_until_repeat(self):
        while self.index not in self._visited_indexes:
            if self.index == len(self.instructions):
                self.state = ComputerState.Terminated
                return

            instr = self.instructions[self.index]

            if instr.op == 'nop':
                self._add_to_index(1)
            elif instr.op == 'jmp':
                self._add_to_index(instr.arg)
            elif instr.op == 'acc':
                self.accumulator += instr.arg
                self._add_to_index(1)
        
        self.state = ComputerState.Paused


def get_first_terminating_program_mod(instruction_strs):
    jmp_or_nop_lines = [
        i for i, s in enumerate(instruction_strs)
        if s.startswith('nop') or s.startswith('jmp')
    ]

    for line in jmp_or_nop_lines:
        modified_program = instruction_strs.copy()
        orig, new = modified_program[line].startswith('nop') and ('nop', 'jmp') or ('jmp', 'nop')
        modified_program[line] = modified_program[line].replace(orig, new)

        program = BootCodeComputer(modified_program)
        program.run_until_repeat()

        if program.state == ComputerState.Terminated:
            return program

    return None


if __name__ == '__main__':
    data = get_data(8, entry_trans=str)
    computer = BootCodeComputer(data)
    computer.run_until_repeat()

    print(f'Part 1:  {computer.accumulator}')

    terminating_computer = get_first_terminating_program_mod(data)
    print(f'Part 2:  {terminating_computer.accumulator}')
