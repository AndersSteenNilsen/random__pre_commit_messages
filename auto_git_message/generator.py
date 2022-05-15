from ast import arg
from typing import Sequence
import sys
import subprocess


def generate_message(commit_message_filename=sys.argv[1]):
    print(sys.argv[1:])
    diff = subprocess.run(['git', 'diff'], capture_output=True).stdout
    print(diff)
    with open(commit_message_filename, 'w+') as f:
        f.write('!')
    return 0


if __name__ == '__main__':
    exit()
