import sys
import fileinput

'''
python 05_2.py input_05.txt
'''


def get_lowest_location(cards: list) -> int:
    _sum = 0
    return _sum


def main():
    result = 0
    cards = []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            cards.append(line)

    result += get_lowest_location(cards)

    # Demo
    assert result == 35
    '''
    # Final
    assert result == TBD
    '''

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
