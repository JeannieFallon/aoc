import sys
import fileinput

'''
python 01_2.py input_01.txt
'''

DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_sum_calib_vals():
    _sum = 0

    with fileinput.input(encoding="utf-8") as f:

        for line in f:
            d1, d2 = '', ''

            '''This is total spaghetti but I'm too tired to make it pretty'''

            for i, c1 in enumerate(line):
                if c1.isdigit():
                    d1 = c1
                    break
                else:
                    for word in DIGIT_WORDS:
                        if word in line[:i+1]:
                            d1 = str(DIGIT_WORDS.index(word))
                            break
                if d1:
                    break

            rev_line = line[::-1]
            for j, c2 in enumerate(rev_line):
                if c2.isdigit():
                    d2 = c2
                    break
                else:
                    for word in DIGIT_WORDS:
                        if word[::-1] in rev_line[:j+1]:
                            d2 = str(DIGIT_WORDS.index(word))
                            break
                if d2:
                    break

            _sum += int(d1+d2)

    return _sum


def main():
    result = get_sum_calib_vals()

    '''
    # Demo
    assert result == 281
    '''
    # Final
    assert result == 53894
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
