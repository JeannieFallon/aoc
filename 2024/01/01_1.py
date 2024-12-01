import sys
import fileinput

'''
python 01_1.py input_01.txt
'''

def get_total_distance(left: list, right: list) -> int:
    total = 0

    left.sort()
    right.sort()

    for i in (range(len(left))):
        total += abs(left[i] - right[i])

    return total


def main() -> int:
    left, right = [], []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            vals = line.split()
            left.append(int(vals[0]))
            right.append(int(vals[1]))

    if len(left) != len(right):
        raise ValueError("Left and right lists are of different lengths! Cannot compare")

    result = get_total_distance(left, right)

    '''
    # Demo
    assert result == 11
    '''
    print(f'Success for result: {result}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
