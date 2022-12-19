import sys
import pathlib

'''
python 05_2.py crates.txt moves.txt
'''

def parse_move(move: str):
    #FIXME use regex re.compile(''.join(map()))
    vals = [int(val) for val in move[5:].replace('from','').replace('to','').split()]
    return vals[0], vals[1] - 1, vals[2] - 1


def get_stacks(crate_lines: list):
    stack_ids = crate_lines.pop().split()
    if int(stack_ids[0]) != 1:
        raise ValueError(f"Error with stack numbers in initial crate data: {stack_ids}")

    num_stacks = len(stack_ids)
    stacks = [[] for j in [[] for i in range(num_stacks)]]

    step = 3
    for line in reversed(crate_lines):
        c = 0
        for idx in range(num_stacks):
            if line[c] == '[':
                stacks[idx].append(line[c:c+step].strip('[').strip(']'))
            c += step + 1

    return stacks


def get_top_crates(stacks: list, moves: list):
    top_crates = ''

    for move in moves:
        num, src, dst = parse_move(move)
        len_src = len(stacks[src])
        crates_to_move = stacks[src][len_src-num:len_src]
        stacks[dst] += crates_to_move
        stacks[src] = stacks[src][:len_src-num]

    for stack in stacks:
        for idx, crate in enumerate(reversed(stack)):
            top_crates += crate[idx]
            break

    return top_crates


def main():
    if len(sys.argv) < 3:
        raise FileNotFoundError("Usage: 05_2.py crates.txt moves.txt")
    crates_file = pathlib.Path(sys.argv[1])
    moves_file = pathlib.Path(sys.argv[2])

    crate_input = []
    with crates_file.open() as cf:
        crate_input = [i.strip('\n') for i in cf.readlines()]

    moves = []
    with moves_file.open() as mf:
        moves = [i.strip('\n') for i in mf.readlines()]

    stacks = get_stacks(crate_input)
    result = get_top_crates(stacks, moves)

    assert result == 'CDTQZHBRS'
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
