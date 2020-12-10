from ..aoc_util import get_data
from itertools import product


class XmasCypher:
    def __init__(self, data, preamble_len=25):
        self.preamble_len = preamble_len
        self.data = data
        self.index = preamble_len

    def _current_window(self):
        return self.data[self.index - self.preamble_len: self.index]

    @property
    def current_val(self):
        return self.data[self.index]

    def check_next(self):
        is_valid = self.current_val in [
            x + y for x, y in product(self._current_window(), self._current_window())
            if x != y    
        ]

        self.index += 1

        return is_valid

    def find_contiguous_sublist_summing_to(self, num):
        for i in range(len(self.data) - 1):
            for j in range(i + 1, len(self.data)):
                this_sublist = self.data[i:j]
                if sum(this_sublist) == num:
                    return this_sublist

        return None
        

if __name__ == '__main__':
    data = get_data(9, entry_trans=int)
    cypher = XmasCypher(data)

    first_invalid = None
    while first_invalid == None:
        val = cypher.current_val
        if not cypher.check_next():
            first_invalid = val

    print(f'Part 1:  {first_invalid}')

    contiguous_sublist = cypher.find_contiguous_sublist_summing_to(first_invalid)

    print(f'Part 2:  {min(contiguous_sublist) + max(contiguous_sublist)}')
