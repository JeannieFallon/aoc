import sys
import fileinput

'''
python 08_2.py input_08.txt
'''

def get_scenic_score(matrix):

    max_score = 0
    row_len = len(matrix[0])
    col_len = len(matrix)

    for i, row in enumerate(matrix):
        # Viewing score of 0 on edge
        if i == 0 or i == col_len - 1:
            continue

        for j, col in enumerate(row):
            # Viewing score of 0 on edge
            if j == 0 or j == row_len - 1:
                continue

            curr = matrix[i][j]
            curr_score = 0

            # Split row to left and right of curr tree
            _row = matrix[i].copy()
            left = _row[:j]
            right = _row[j+1:]

            # Build current column and split to top and bottom of curr tree
            col = []
            for ii in range(0, col_len):
                col.append(matrix[ii][j])

            _col = col.copy()
            top = _col[:i]
            bott = _col[i+1:]

            # Left score
            left_score = 0
            for l in left[::-1]:
                left_score += 1
                if curr <= l:
                    break

            # Right score
            right_score = 0
            for r in right:
                right_score += 1
                if curr <= r:
                    break

            # Top score
            top_score = 0
            for t in top[::-1]:
                top_score += 1
                if curr <= t:
                    break

            # Bottom score
            bott_score = 0
            for b in bott:
                bott_score += 1
                if curr <= b:
                    break

            curr_score = left_score * right_score * top_score * bott_score

            if curr_score > max_score:
                max_score = curr_score

    return max_score


def main():
    matrix = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            matrix.append([int(i) for i in line.strip()])

    result = get_scenic_score(matrix)


    assert result == 180000
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
