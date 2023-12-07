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


SPEC_CHARS = '[@_!#$%^&*()<>?/\|}{~:]'


def check_adjacent(num: Number, matrix: list) -> bool:
    #FIXME debug
    print(num.__repr__())

    # Iterate over list of Number indices
    for idx in num.indices:

    # Check adjacent spaces in matrix for special chars

        #FIXME debug
        #print(matrix[idx[0]][idx[1]])
        # First row of matrix
        if idx[0] < 1:
            print(f'first row: {idx[0]}')
        # Final row of matrix
        elif idx[0] == len(matrix) - 1:
            print(f'final row: {idx[0]}')

    # If find special char in adjacent space, break and return True
        if False:
            return True

    return False


def get_sum_part_nums(matrix: list) -> int:
    _sum = 0

    # Iterate over each line of engine schematic
    for i, line in enumerate(matrix):

        # Create first possible number in line
        num = Number()

        for j, char in enumerate(line):

            # If digit, collect as part of a number
            if char.isdigit():
                num.value += char
                num.indices.append((i, j))

            # If not digit, only check if a number has been collected
            elif num.value:
                if (check_adjacent(num, matrix)):
                    _sum += int(num.value)

                # Reset placeholder string for next number
                num = Number()

        #FIXME debug break to isolate first line
        #break

    return _sum


def main():
    matrix = []
    result = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Create nested lists of engine schematic
            matrix.append([i for i in line.strip()])

    result = get_sum_part_nums(matrix)

    # Demo
    assert result == 4361
    '''
    # Final
    assert result == 2716
    '''

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
