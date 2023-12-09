import sys
import math
import fileinput

from dataclasses import dataclass, field

'''
python 03_2.py input_03.txt
'''

@dataclass
class Gear:
    symbol: str = '*'
    idx: tuple = field(default_factory=tuple)


def check_row_above(x: int, y: int, matrix: list) -> int:
    # Skip if in first row of matrix
    if x == 0:
        return 0

    # Iterate over adjacent cols in row above
    for i in range(-1, 1):
        if matrix[x-1][y+i].isdigit():
            return 1

    return 0


def check_row_curr(x: int, y: int, matrix: list) -> int:
    # Check column before
    if not y == 0:
        if matrix[x][y-1].isdigit():
            return 1

    # Check column after
    if not y == len(matrix[0]) - 1:
        if matrix[x][y+1].isdigit():
            return 1

    return 0


def check_row_below(x: int, y: int, matrix: list) -> int:
    # Skip if in last row of matrix
    if x == len(matrix) - 1:
        return 0

    # Iterate over adjacent cols in row below
    for i in range(-1, 1):
        if matrix[x+1][y+i].isdigit():
            return 1

    return 0


def check_adjacent(gear: Gear, matrix: list) -> int:
    nums = []

    # Pull coords for easier logic
    x, y = gear.idx[0], gear.idx[1]

    # Row above
    nums.append(check_row_above(x, y, matrix))

    # Curr row
    nums.append(check_row_curr(x, y, matrix))

    # Row below
    nums.append(check_row_below(x, y, matrix))

    # Purge any dummy zeroes
    nums = [x for x in nums if x > 0]

    if len(nums) > 0 and len(nums) < 3:
        return math.prod(nums)

    return 0


def get_sum_gear_ratios(matrix: list) -> int:
    gear = Gear()
    _sum = 0

    # Iterate over each line of engine schematic
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            # If gear, check adjacent for number
            if char == gear.symbol:
                gear.idx = (i, j)
                _sum += check_adjacent(gear, matrix)

    return _sum


def main():
    matrix = []
    result = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Create nested lists of engine schematic
            matrix.append([l for l in line.strip()])

    result = get_sum_gear_ratios(matrix)

    # Demo
    #assert result == 467835
    '''
    # Final
    assert result == 525911
    '''

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
