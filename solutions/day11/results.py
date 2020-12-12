import itertools
from ..aoc_util import get_data


EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'


class Grid(list):
    def get_val(self, coord):
        return self[coord[0]][coord[1]]

    def set_val(self, coord, val):
        row_list = list(self[coord[0]])
        row_list[coord[1]] = val
        new_row = ''.join(row_list)

        self[coord[0]] = new_row


class TerminalSeating:
    def __init__(self, initial):
        self.initial = Grid(initial)
        self.current = Grid(initial.copy())
        self.epoch = 0
        self.equilibrium_epoch = None

        self.dims = len(initial), len(initial[0])

    def run_epoch(self):
        new = Grid(self.current.copy())

        for coord in itertools.product(*[range(z) for z in self.dims]):
            val = self.current.get_val(coord)
            adj_occ_seats = self._get_num_adjacent_occupied_seats(coord)

            if val == EMPTY_SEAT and adj_occ_seats == 0:
                new.set_val(coord, OCCUPIED_SEAT)
            elif val == OCCUPIED_SEAT and adj_occ_seats >= 4:
                new.set_val(coord, EMPTY_SEAT)

        self.current = new
        self.epoch += 1

    def run_epochs(self, num_epochs):
        for _ in range(num_epochs):
            self.run_epoch()

    def run_until_equilibrium(self):
        while self.equilibrium_epoch is None:
            current_copy = self.current.copy()
            self.run_epoch()
            if current_copy == self.current:
                self.equilibrium_epoch = self.epoch

    def _get_num_adjacent_occupied_seats(self, coord):
        num_adjacent_occupied_seats = 0

        dim_adjs = [1, 0, -1]
        for adj in itertools.product(dim_adjs, dim_adjs):
            this_coord = tuple(sum(z) for z in zip(coord, adj))

            # Disqualify trivial/invalid adjustments
            if any([
                adj == (0, 0),
                this_coord[0] not in range(self.dims[0]),
                this_coord[1] not in range(self.dims[1]),
            ]):
                continue

            if self.current.get_val(this_coord) == OCCUPIED_SEAT:
                num_adjacent_occupied_seats += 1

        return num_adjacent_occupied_seats


if __name__ == '__main__':
    data = get_data(11, entry_trans=str)
    seating = TerminalSeating(data)
    seating.run_until_equilibrium()
    num_seats_occupied = sum([len([z for z in row if z == OCCUPIED_SEAT]) for row in seating.current])
    print(f'Part 1:  {num_seats_occupied}')

    print(f'Part 2:  NOT IMPLEMENTED')
