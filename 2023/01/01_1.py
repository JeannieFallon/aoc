import sys
import fileinput

'''
python 01_1.py input_01.txt
'''

def get_sum_calib_vals():
    _sum = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            for c1 in line:
                if c1.isdigit():
                    break
            for c2 in reversed(line):
                if c2.isdigit():
                    break
            _sum += int(c1+c2)

    return _sum


def main():
    result = get_sum_calib_vals()

    '''
    # Demo
    assert result == 142
    '''
    # Final
    assert result == 53651
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
