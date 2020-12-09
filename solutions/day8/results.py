from ..aoc_util import get_data
import collections
import re


class BootCodeComputer:
    def __init__(self, instruction_strs):
        instr_ptn = re.compile('(nop|acc|jmp) ([+-]\d+)')
        Instruction = collections.namedtuple('Instruction', 'op arg')

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
            instr = self.instructions[self.index]

            if instr.op == 'nop':
                self._add_to_index(1)
            elif instr.op == 'jmp':
                self._add_to_index(instr.arg)
            elif instr.op == 'acc':
                self.accumulator += instr.arg
                self._add_to_index(1)


if __name__ == '__main__':
    data = get_data(8, entry_trans=str)
    computer = BootCodeComputer(data)
    computer.run_until_repeat()

    print(f'Part 1:  {computer.accumulator}')

    print(f'Part 2:  NOT IMPLEMENTED')
