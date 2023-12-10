import sys
import fileinput

'''
python 04_1.py input_04.txt
'''


def get_total_points(wins: list, nums: list) -> int:
    _sum, hits = 0, 0

    # Iterate over nums and check if in wins list
    for num in nums:
        if num in wins:
            hits += 1

    return _sum if not hits else 2**(hits-1)


def main():
    result = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Parse each line into lists of winning nums and nums you have
            wins, nums = line.split('|')
            wins = [int(w) for w in wins.split(':')[1].strip().split()]
            nums = [int(n) for n in nums.strip().split()]

            result += get_total_points(wins, nums)


    '''
    # Demo
    assert result == 13
    '''
    # Final
    assert result == 26914

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
