from ..aoc_util import get_data


class NavInstruction:
    def __init__(self, direction, magnitude):
        valid_directions = ('N', 'S', 'E', 'W', 'L', 'R', 'F')
        if direction not in valid_directions:
            raise ValueError(f'NavInstruction direction must be in {valid_directions}')

        self.direction = direction
        self.magnitude = magnitude

    @staticmethod
    def from_str(instr_str):
        direction = instr_str[0]
        magnitude = int(instr_str[1:])

        return NavInstruction(direction, magnitude)

    def __repr__(self):
        return f'<NavInstruction(direction={self.direction}, magnitude={self.magnitude})>'


class Ship:
    def __init__(self):
        self.position = [0, 0]
        self.direction = 'E'

        self._cardinal_order = ['N', 'E', 'S', 'W']

    def navigate(self, instrs):
        # Handle single instruction or list
        if isinstance(instrs, (list, tuple)):
            for instr in instrs:
                self._navigate(instr)
        else:
            self.navigate(instrs)

    def _navigate(self, instr):
        if instr.direction == 'N':
            self.position[1] += instr.magnitude
        elif instr.direction == 'S':
            self.position[1] -= instr.magnitude
        elif instr.direction == 'E':
            self.position[0] += instr.magnitude
        elif instr.direction == 'W':
            self.position[0] -= instr.magnitude
        elif instr.direction in ('L', 'R'):
            num_turns = instr.magnitude // 90
            index_offset = (instr.direction == 'L' and -1 or 1) * num_turns

            new_dir_index = (self._cardinal_order.index(self.direction) + index_offset) \
                % (len(self._cardinal_order))

            self.direction = self._cardinal_order[new_dir_index]
        else:
            # 'F'
            new_nav_instr = NavInstruction(self.direction, instr.magnitude)
            self._navigate(new_nav_instr)


if __name__ == '__main__':
    data = get_data(12, entry_trans=NavInstruction.from_str)
    ship = Ship()
    ship.navigate(data)

    manhattan_distance = abs(ship.position[0]) + abs(ship.position[1])

    print(f'Part 1:  {manhattan_distance}')

    print(f'Part 2:  NOT IMPLEMENTED')
