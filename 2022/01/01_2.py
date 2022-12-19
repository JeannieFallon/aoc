import sys
import fileinput

'''
python 01_2.py input_01.txt
'''

def get_max_cals():
    cals = 0
    top_cals = [0,0,0]

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            if line == '\n':
                if cals > top_cals[0]:
                    top_cals[0] = cals
                    top_cals.sort()
                cals = 0
                continue
            cals += int(line)

    return sum(top_cals)


def main():
    result = get_max_cals()

    assert result == 207148
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
