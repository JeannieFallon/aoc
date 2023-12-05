import sys
import fileinput

'''
python 02_1.py input_02.txt
'''

MAX_VALS = {
    "blue": 14,
    "green": 13,
    "red": 12,
}


def check_max_vals(set: str) -> bool:
    # Get number of color from each set
    num_color = set.split(',')

    for num_color in num_color:
        num, color = num_color.split()
        if MAX_VALS[color] < int(num):
            return False

    return True


def check_sets(sets: str) -> bool:
    # Check each individual set
    for set in sets:
        if not check_max_vals(set):
            return False

    return True


def get_sum_ids() -> int:
    _sum = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            game, results = line.strip().split(':')

            # Get game ID
            _id = int(game.split()[1])

            # Get individual sets
            sets = results.split(';')

            # Break if any set has an impossible value
            if not check_sets(sets):
                continue

            # Add game ID only if no color exceeds max possible
            _sum += _id

    return _sum


def main():
    result = get_sum_ids()

    '''
    # Demo
    assert result == 8
    '''
    # Final
    assert result == 2716

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
