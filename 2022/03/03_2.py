import sys
import string
import fileinput

'''
python 03_2.py input_03.txt
'''

ALPHA = string.ascii_letters

def get_priority(group):
    badge = ''

    for c in group[0]:
        if c in group[1]  and c in group[2]:
            badge = c
            break

    return (ALPHA.find(badge) + 1)


def get_priorities_sum():
    _sum = 0
    lines = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            lines.append(line)

    # split into groups of 3
    group_size = 3
    groups = [lines[i:i + group_size] for i in range(0, len(lines), group_size)]

    for group in groups:
        _sum += get_priority(group)

    return _sum


def main():
    result = get_priorities_sum()

    assert result == 2716
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
