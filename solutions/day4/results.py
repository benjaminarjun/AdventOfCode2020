from ..aoc_util import get_data
import re


def _is_valid_passport(passport, with_data_validation):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport_dict = {kvp.split(':')[0]: kvp.split(':')[1] for kvp in passport.split()}

    has_required_keys = all([key in passport_dict.keys() for key in required_keys])
    
    if not with_data_validation or not has_required_keys:
        return has_required_keys
    
    # data validation
    d = passport_dict

    if not 1920 <= int(d['byr']) <= 2002:
        return False

    if not 2010 <= int(d['iyr']) <= 2020:
        return False

    if not 2020 <= int(d['eyr']) <= 2030:
        return False

    hgt_match = re.match('(\d+)(cm|in)', d['hgt'])
    if hgt_match is None:
        return False
    elif hgt_match.group(2) == 'cm' and not 150 <= int(hgt_match.group(1)) <= 193:
        return False
    elif hgt_match.group(2) == 'in' and not 59 <= int(hgt_match.group(1)) <= 76:
        return False
    
    if re.match(r'#[0-9a-f]{6}', d['hcl']) is None:
        return False
    
    if d['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if len(d['pid']) != 9:
        return False
    
    return True


def get_num_valid_passports(batch_file, with_data_validation=False):
    passports = []

    passport = ''
    for line in batch_file:
        if line == '':
            passports.append(passport)
            passport = ''
        else:
            if passport == '':
                passport = line
            else:
                passport += ' ' + line

    # Add any leftovers as a full passport
    if passport != '':
        passports.append(passport)

    return len([p for p in passports if _is_valid_passport(p, with_data_validation)])


if __name__ == '__main__':
    batch_file = get_data(4, entry_trans=str)
    num_valid_passports = get_num_valid_passports(batch_file)

    print(f'Part 1:  {num_valid_passports}')

    num_valid_passports_w_valid_data = get_num_valid_passports(batch_file, with_data_validation=True)

    print(f'Part 2:  {num_valid_passports_w_valid_data}')
