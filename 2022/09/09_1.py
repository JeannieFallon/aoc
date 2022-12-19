import sys
import fileinput

'''
python 09_1.py input_09.txt
'''

def update_matrix(matrix: list, tail: list):
    '''Mark tail position as visited on matrix'''
    matrix[tail[0]][tail[1]] = 1
    return matrix


def walk_matrix(matrix: list):
    '''Visited positions = 1, Not visited = 0'''
    positions = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j]:
                positions += 1

    return positions

#FIXME combine these
def exec_move_up(steps: int, matrix: list, head: list, tail: list):
    # Decrement head X point
    for step in range(steps):
        head[0] -= 1

        # Make tail follow
        if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) == 1:
            tail[1] = head[1]

            if tail[0] > head[0]:
                tail[0] -= 1
            else:
                tail[0] += 1

        elif abs(head[0] - tail[0]) > 1 and head[1] == tail[1]:
            tail[0] -= 1

        matrix = update_matrix(matrix, tail)

    return matrix, head, tail


def exec_move_down(steps: int, matrix: list, head: list, tail: list):
    # Increment head X point
    for step in range(steps):
        head[0] += 1

        # Make tail follow
        if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) == 1:
            tail[1] = head[1]

            if tail[0] > head[0]:
                tail[0] -= 1
            else:
                tail[0] += 1

        elif abs(head[0] - tail[0]) > 1 and head[1] == tail[1]:
            tail[0] += 1

        matrix = update_matrix(matrix, tail)

    return matrix, head, tail


def exec_move_left(steps: int, matrix: list, head: list, tail: list):
    # Decrement head Y point
    for step in range(steps):
        head[1] -= 1

        # Make tail follow
        if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) > 1:
            tail[0] = head[0]

            if tail[1] > head[1]:
                tail[1] -= 1
            else:
                tail[1] += 1

        elif abs(head[1] - tail[1]) > 1 and head[0] == tail[0]:
            tail[1] -= 1

        #print(f'>> AFTER L_move step {step} >> head, tail: {head, tail}')
        matrix = update_matrix(matrix, tail)

    return matrix, head, tail


def exec_move_right(steps: int, matrix: list, head: list, tail: list):
    # Increment head Y point
    for step in range(steps):
        #FIXME
        head[1] += 1

        # Make tail follow
        if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) > 1:
            tail[0] = head[0]

            if tail[1] > head[1]:
                tail[1] -= 1
            else:
                tail[1] += 1

        elif abs(head[1] - tail[1]) > 1 and head[0] == tail[0]:
            tail[1] += 1

        matrix = update_matrix(matrix, tail)

    return matrix, head, tail


def parse_move(move: list, head: list, tail: list, matrix: list):
    '''Get direction of moves, then execute for num steps'''
    direction = move[0]
    steps = move[1]

    match direction:
        case 'L':
            matrix, head, tail = exec_move_left(steps, matrix, head, tail)
        case 'R':
            matrix, head, tail = exec_move_right(steps, matrix, head, tail)
        case 'U':
            matrix, head, tail = exec_move_up(steps, matrix, head, tail)
        case 'D':
            matrix, head, tail = exec_move_down(steps, matrix, head, tail)

    return head, tail, matrix


def get_tail_positions(moves):
    positions = 0

    # Build a stupid big matrix
    col_len, row_len = 1000, 1000
    matrix = [[0 for i in range(row_len)] for j in range(col_len)]

    # Starting position for both head and tail, middle of matrix
    head, tail = [500,500], [500,500]
    matrix = update_matrix(matrix, tail)

    for move in moves:
        head, tail, matrix = parse_move(move, head, tail, matrix)

    positions = walk_matrix(matrix)

    return positions


def main():
    moves = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            line = line.split()
            moves.append([line[0], int(line[1])])

    result = get_tail_positions(moves)

    assert result == 6212
    print(f'Success for result: {result}')

if __name__ == "__main__":
    main()
