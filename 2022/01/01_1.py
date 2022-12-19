import sys
import fileinput

'''
python 01_1.py input_01.txt
'''

def get_max_cals():
    cals = 0
    max_cals = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            if line == '\n':
                if cals > max_cals:
                    max_cals = cals
                cals = 0
                continue
            cals += int(line)

    return max_cals


def main():
    result = get_max_cals()

    assert result == 70720
    print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
