import sys
import fileinput

from dataclasses import dataclass, field

'''
python 03_1.py input_03.txt
'''

@dataclass
class Number:
    value: str = ''
    length: int = 0
    indices: list[tuple] = field(default_factory=list)


SPEC_CHARS = {'@', '#', '-', '&', '$', '/', '+', '%', '=', '*'}


def check_row_above(x: int, y: int, num: Number, matrix: list) -> bool:
    # Skip if in first row of matrix
    if x == 0:
        return False

    # Check column before
    if not y == 0:
        if matrix[x-1][y-1] in SPEC_CHARS:
            return True

    # Iterate over adjacent cols in row above
    for c in range(num.length):
        if matrix[x-1][y+c] in SPEC_CHARS:
            return True

    # Check column after
    if not y == len(matrix[0]) - 1:
        if matrix[x-1][y+1] in SPEC_CHARS:
            return True

    return False


def check_row_curr(x: int, y: int, matrix: list) -> bool:
    # Check column before
    if not y == 0:
        if matrix[x][y-1] in SPEC_CHARS:
            return True

    # Check column after
    if not y == len(matrix[0]) - 1:
        if matrix[x][y+1] in SPEC_CHARS:
            return True

    return False


def check_row_below(x: int, y: int, num: Number, matrix: list) -> bool:
    # Skip if in last row of matrix
    if x == len(matrix) - 1:
        return False

    # Check column before
    if not y == 0:
        if matrix[x+1][y-1] in SPEC_CHARS:
            return True

    # Iterate over adjacent cols in row above
    for c in range(num.length):
        if matrix[x+1][y+c] in SPEC_CHARS:
            return True

    # Check column after
    if not y == len(matrix[0]) - 1:
        if matrix[x+1][y+1] in SPEC_CHARS:
            return True

    return False


#FIXME numbers on beginning and end of line aren't hitting
def check_adjacent(num: Number, matrix: list) -> bool:
    # Iterate over list of Number indices
    for idx in num.indices:

        # Pull coords for easier logic
        x, y = idx[0], idx[1]

        # Row above
        if check_row_above(x, y, num, matrix):
            return True

        # Curr row
        if check_row_curr(x, y, matrix):
            return True

        # Row below
        if check_row_below(x, y, num, matrix):
            return True

    return False


def get_sum_part_nums(matrix: list) -> int:
    _sum = 0

    #FIXME
    nums = []

    # Iterate over each line of engine schematic
    for i, line in enumerate(matrix):

        # Create first possible number in line
        num = Number()

        for j, char in enumerate(line):

            # If digit, collect as part of a number
            if char.isdigit():
                num.value += char
                num.indices.append((i, j))

            # Check if at end of a number
            elif num.value:
                # Check rows above, current, and below
                if (check_adjacent(num, matrix)):

                    #FIXME
                    nums.append(num.value)

                    _sum += int(num.value)

                # Reset object for next number
                num = Number()

    #FIXME
    print(nums)
    return _sum


def main():
    matrix = []
    result = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Create nested lists of engine schematic
            matrix.append([l for l in line.strip()])

    result = get_sum_part_nums(matrix)

    # Demo
    #assert result == 4361
    '''
    # Final
    assert result == TBD
    518146 wrong
    521979 wrong
    '''

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
