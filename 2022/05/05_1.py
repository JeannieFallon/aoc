import sys
import pathlib

'''
python 05_1.py crates.txt moves.txt
'''

CRATE = '[0]'

def parse_move(move: str):
    '''Get number of crates to move, source stack, and destination stack'''
    #FIXME use regex re.compile(''.join(map()))
    vals = [int(val) for val in move[5:].replace('from','').replace('to','').split()]

    return vals[0], vals[1] - 1, vals[2] - 1


def get_stacks(crate_lines: list):
    '''Parse crates diagram into nested listed'''
    stack_ids = crate_lines.pop().split()
    if int(stack_ids[0]) != 1:
        raise ValueError(f"Error with stack numbers in initial crate data: {stack_ids}")

    num_stacks = len(stack_ids)
    stacks = [[] for i in range(num_stacks)]

    step = len(CRATE)
    for line in reversed(crate_lines):
        c = 0
        for idx in range(num_stacks):
            if line[c] == '[':
                stacks[idx].append(line[c:c+step].strip('[').strip(']'))
            c += step + 1

    return stacks


def get_top_crates(crates: list, moves: list):
    stacks = get_stacks(crates)

    for move in moves:
        num, src, dst = parse_move(move)
        for n in range(num):
            stacks[dst].append(stacks[src].pop())

    top_crates = ''
    for stack in stacks:
        for idx, crate in enumerate(reversed(stack)):
            top_crates += crate[idx]
            break

    return top_crates


def main():
    if len(sys.argv) < 3:
        raise FileNotFoundError("Usage: 05_1.py crates.txt moves.txt")
    crates_file = pathlib.Path(sys.argv[1])
    moves_file = pathlib.Path(sys.argv[2])

    crates = []
    with crates_file.open() as cf:
        crates = [i.strip('\n') for i in cf.readlines()]

    moves = []
    with moves_file.open() as mf:
        moves = [i.strip('\n') for i in mf.readlines()]

    result = get_top_crates(crates, moves)

    assert result == 'SHQWSRBDL'
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
