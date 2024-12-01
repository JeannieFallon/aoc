import sys
import fileinput

'''
python 01_1.py input_01.txt
'''

def get_similarity_score(left: list, right: list) -> int:
    score = 0

    '''
    Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
    '''

    for i in (range(len(left))):
        ctr = 0
        lval = left[i]
        for rval in right:
            if rval == lval:
                ctr += 1
        score += lval * ctr

    return score


def main() -> int:
    left, right = [], []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            vals = line.split()
            left.append(int(vals[0]))
            right.append(int(vals[1]))

    if len(left) != len(right):
        raise ValueError("Left and right lists are of different lengths! Cannot compare")

    result = get_similarity_score(left, right)

    '''
    # Demo
    assert result == 31
    '''
    print(f'Success for result: {result}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
