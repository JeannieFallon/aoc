import sys
import fileinput

'''
python 02_2.py input_02.txt
'''


def get_game_power(sets: str) -> int:
    # Start with 1 as neutral multiplication base
    power = 1

    # Placeholders for highest number of each color in game
    max_vals = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }

    for set in sets:
        num_color = set.split(',')

        for num_color in num_color:
            num, color = num_color.split()
            num = int(num)
            if num > max_vals[color]:
                max_vals[color] = num

    for val in max_vals.values():
        power = power * val

    return power


def get_sum_powers() -> int:
    _sum = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Get list of sets from game
            sets = line.strip().split(':')[1].split(';')
            _sum +=  get_game_power(sets)

    return _sum


def main():
    result = get_sum_powers()

    '''
    # Demo
    assert result == 2286
    '''
    # Final
    assert result == 72227

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
