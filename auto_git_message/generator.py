
from ast import arg
from typing import Sequence


def generate_message(argv: Sequence[str] | None = None):
    print(argv)
    print('asdfasdfas')
    return 1


if __name__ ==  '__main__':
    print(generate_message())