import re
from ..aoc_util import get_data


class Password:
    def __init__(self, pw_str):
        ptn = re.compile('(\d+)-(\d+) (\w): (\w+)')
        match = re.match(ptn, pw_str)

        if match is None:
            raise Exception('Password string does not match expected format')

        self.letter = match.group(3)
        self.num_1 = int(match.group(1))
        self.num_2 = int(match.group(2))
        self.pw = match.group(4)

        self.pw_str = pw_str

    def is_valid_sled_pw(self):
        occurrences = len([z for z in self.pw if z == self.letter])
        return self.num_1 <= occurrences <= self.num_2

    def is_valid_toboggan_pw(self):
        # subtract 1 since PWs are 1-indexed
        lh_ix = self.num_1 - 1
        rh_ix = self.num_2 - 1

        occurrences = [z for z in (lh_ix, rh_ix) if self.pw[z] == self.letter]
        return len(occurrences) == 1


if __name__ == '__main__':
    data = get_data(2, entry_trans=str)

    num_valid_sled_pws = len([pw for pw in data if Password(pw).is_valid_sled_pw()])
    print(f'Part 1:  {num_valid_sled_pws}')

    num_valid_toboggan_pws = len([pw for pw in data if Password(pw).is_valid_toboggan_pw()])
    print(f'Part 2:  {num_valid_toboggan_pws}')
