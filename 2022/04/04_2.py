import sys
import fileinput

'''
python 04_2.py input_04.txt
'''

def check_overlap(pair):
    vals = [int(i) for i in pair.strip().replace('-',',').split(',')]
    return vals[1] >= vals[2] and not vals[3] < vals[0]

def get_overlapping_pairs():
    pairs = 0
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            pairs += check_overlap(line)

    return pairs


def main():
    result = get_overlapping_pairs()

    assert result == 808
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
