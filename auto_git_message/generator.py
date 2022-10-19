from ast import arg
import random
from typing import Sequence
import sys

COMMITS_PATH = 'auto_git_message/commit_messages.txt'
def get_random_commit_message():
    with open(COMMITS_PATH) as file_input:
        commit_messages = file_input.readlines()
    
    return random.choice(commit_messages).strip()

def generate_message(commit_message_filename=sys.argv[-1]):
    print(sys.argv)
    with open(commit_message_filename, 'r') as f:
        commit_message = f.read().strip()
    if commit_message != 'random':
        return 0
    with open(commit_message_filename, 'w') as f:
        random_message = get_random_commit_message()
        f.write(random_message)
    return 0

# comment
if __name__ == '__main__':
    exit()
