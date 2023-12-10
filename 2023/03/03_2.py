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


def get_number(matrix: list, x: int, y: int) -> (int, int):
    # Build number as string
    num = ''

    # Iterate backward along row from starting coordinate
    _y = y
    while _y >= 0:
        if matrix[x][_y].isdigit():
            num = matrix[x][_y] + num
            _y -= 1
        else:
            break

    # Iterate forward along row from starting coordinate
    _y = y + 1
    while _y < len(matrix[0]):
        if matrix[x][_y].isdigit():
            num = num + matrix[x][_y]
            _y += 1
        else:
            break

    # Need to know what Y coord number ends on
    return int(num), _y


def check_row_above(x: int, y: int, matrix: list) -> int:
    # Skip if in first row of matrix
    if x == 0:
        return 0

    # Need to account for multiple nums in the same row
    nums = []

    # Iterate over adjacent cols in row above
    i = -1
    while i <= 1:
        # Get the coordinate in matrix
        mx = x - 1
        my = y + i

        if matrix[mx][my].isdigit():
            num, num_y = get_number(matrix, mx, my)
            nums.append(num)
            i += num_y - my

        i += 1

    return nums


def check_row_curr(x: int, y: int, matrix: list) -> int:
    # Need to account for multiple nums in the same row
    nums = []

    # Check column before
    if not y == 0:
        # Get the coordinate in matrix
        mx = x
        my = y - 1

        if matrix[mx][my].isdigit():
            num, _ = get_number(matrix, mx, my)
            nums.append(num)

    # Check column after
    if not y == len(matrix[0]) - 1:
        # Get the coordinate in matrix
        mx = x
        my = y + 1

        if matrix[mx][my].isdigit():
            num, _ = get_number(matrix, mx, my)
            nums.append(num)

    return nums


def check_row_below(x: int, y: int, matrix: list) -> int:
    # Skip if in last row of matrix
    if x == len(matrix) - 1:
        return 0

    # Need to account for multiple nums in the same row
    nums = []

    # Iterate over adjacent cols in row below
    i = -1
    while i <= 1:
        # Get the coordinate in matrix
        mx = x + 1
        my = y + i

        if matrix[mx][my].isdigit():
            num, num_y = get_number(matrix, mx, my)
            nums.append(num)
            i += num_y - my

        i += 1

    return nums


def check_adjacent(gear: Gear, matrix: list) -> int:
    nums = []

    # Pull coords for easier logic
    x, y = gear.idx[0], gear.idx[1]

    # Row above
    nums += check_row_above(x, y, matrix)

    # Curr row
    nums += check_row_curr(x, y, matrix)

    # Row below
    nums += check_row_below(x, y, matrix)

    # Purge any dummy zeroes
    nums = [x for x in nums if x > 0]

    if len(nums) > 1 and len(nums) < 3:
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

    '''
    # Demo
    assert result == 467835
    '''
    # Final
    assert result == 75805607

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
