import sys
import string
import fileinput

'''
python 03_1.py input_03.txt
'''

ALPHA = string.ascii_letters

def get_priority(contents):
    mistake_item = ''

    split = len(contents)//2
    comp_1 = set(contents[:split])
    comp_2 = set(contents[split:])

    for c in comp_1:
        if c in comp_2:
            mistake_item = c
            break

    return (ALPHA.find(mistake_item) + 1)


def get_priorities_sum():
    _sum = 0
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            _sum += get_priority(line)
    return _sum


def main():
    result = get_priorities_sum()

    assert result == 7967
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
