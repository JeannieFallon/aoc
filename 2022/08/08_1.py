import sys
import fileinput

'''
python 08_1.py input_08.txt
'''

def get_visible_trees(matrix):

    vis_trees = 0
    row_len = len(matrix[0])
    col_len = len(matrix)

    for i, row in enumerate(matrix):
        # Add entire row to visible trees
        if i == 0 or i == col_len - 1:
            vis_trees += row_len
            continue

        for j, col in enumerate(row):
            # Add first and last tree in each row
            if j == 0 or j == row_len - 1:
                vis_trees += 1
                continue

            curr = matrix[i][j]

            # Split row to left and right of curr tree
            _row = matrix[i].copy()
            left = _row[:j]
            right = _row[j+1:]
            left_high = sorted(left, reverse=True)[0]
            right_high = sorted(right, reverse=True)[0]

            if curr > left_high or curr > right_high:
                vis_trees += 1
                continue

            # Build current column
            col = []
            for ii in range(0, col_len):
                col.append(matrix[ii][j])

            # Split column to top and bottom of curr tree
            _col = col.copy()
            top = _col[:i]
            bott = _col[i+1:]
            top_high = sorted(top, reverse=True)[0]
            bott_high = sorted(bott, reverse=True)[0]

            if curr > top_high or curr > bott_high:
                vis_trees += 1
                continue

    return vis_trees


def main():
    matrix = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            matrix.append([int(i) for i in line.strip()])

    result = get_visible_trees(matrix)

    assert result == 1843
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
