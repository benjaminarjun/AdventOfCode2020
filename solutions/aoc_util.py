import os
import sys


def _get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def parse_file_contents(content, entry_trans):
    return [entry_trans(z.strip()) for z in content.split('\n')]


def get_data(day, entry_trans=int):
    path = os.path.join(_get_script_path(), '..', '..', 'data', f'day{day}.txt')
    with open(path, 'r') as f:
        return parse_file_contents(f.read(), entry_trans)
