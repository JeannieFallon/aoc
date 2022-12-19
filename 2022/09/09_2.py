import sys
import fileinput

'''
python 09_2.py input_09.txt
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
def exec_move_left(steps: int, matrix: list, rope: list):
    # Decrement head Y point
    for step in range(steps):
        rope[0][1] -= 1

        # Make knots follow
        for i in range(9):
            if abs(rope[i][0] - rope[i+1][0]) == 1 and abs(rope[i][1] - rope[i+1][1]) > 1:
                rope[i+1][0] = rope[i][0]

                if rope[i+1][1] > rope[i][1]:
                    rope[i+1][1] -= 1
                else:
                    rope[i+1][1] += 1

            elif abs(rope[i][1] - rope[i+1][1]) > 1 and rope[i][0] == rope[i+1][0]:
                rope[i+1][1] -= 1

        matrix = update_matrix(matrix, rope[9])

    return matrix, rope


def exec_move_right(steps: int, matrix: list, rope: list):
    #FIXME first move of demo2
    # Increment head Y point
    for step in range(steps):
        rope[0][1] += 1

        # Make knots follow
        for i in range(9):
            if abs(rope[i][0] - rope[i+1][0]) == 1 and abs(rope[i][1] - rope[i+1][1]) > 1:
                rope[i+1][0] = rope[i][0]

                if rope[i+1][1] > rope[i][1]:
                    rope[i+1][1] -= 1
                else:
                    rope[i+1][1] += 1

            elif abs(rope[i][1] - rope[i+1][1]) > 1 and rope[i][0] == rope[i+1][0]:
                rope[i+1][1] += 1

        matrix = update_matrix(matrix, rope[9])

    return matrix, rope


def exec_move_up(steps: int, matrix: list, rope: list):
    # Decrement head X point
    for step in range(steps):
        rope[0][0] -= 1

        # Make knots follow
        for i in range(9):
            if abs(rope[i][0] - rope[i+1][0]) > 1 and abs(rope[i][1] - rope[i+1][1]) == 1:
                rope[i+1][1] = rope[i][1]

                if rope[i+1][0] > rope[i][0]:
                    rope[i+1][0] -= 1
                else:
                    rope[i+1][0] += 1

            elif abs(rope[i][0] - rope[i+1][0]) > 1 and rope[i][1] == rope[i+1][1]:
                rope[i+1][0] -= 1

        matrix = update_matrix(matrix, rope[9])

    return matrix, rope


def exec_move_down(steps: int, matrix: list, rope: list):
    # Increment head X point
    for step in range(steps):
        rope[0][0] += 1

        # Make knots follow
        for i in range(9):
            if abs(rope[i][0] - rope[i+1][0]) > 1 and abs(rope[i][1] - rope[i+1][1]) == 1:
                rope[i+1][1] = rope[i][1]

                if rope[i+1][0] > rope[i][0]:
                    rope[i+1][0] -= 1
                else:
                    rope[i+1][0] += 1

            elif abs(rope[i][0] - rope[i+1][0]) > 1 and rope[i][1] == rope[i+1][1]:
                rope[i+1][0] += 1

        matrix = update_matrix(matrix, rope[9])

    return matrix, rope


def parse_move(move: list, rope: list, matrix: list):
    '''Get direction of moves, then execute for num steps'''
    direction = move[0]
    steps = move[1]

    match direction:
        case 'L':
            matrix, rope = exec_move_left(steps, matrix, rope)
        case 'R':
            matrix, rope = exec_move_right(steps, matrix, rope)
        case 'U':
            matrix, rope = exec_move_up(steps, matrix, rope)
        case 'D':
            matrix, rope = exec_move_down(steps, matrix, rope)

    return matrix


def get_tail_positions(moves):
    positions = 0

    # Build a stupid big matrix
    col_len, row_len = 1000, 1000
    matrix = [[0 for i in range(row_len)] for j in range(col_len)]

    # Starting position for all 10 knots of rope, middle of matrix
    rope = [[500,500] for i in range(10)]
    matrix = update_matrix(matrix, rope[9])

    for move in moves:
        matrix = parse_move(move, rope, matrix)


    positions = walk_matrix(matrix)

    return positions


def main():
    moves = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            line = line.split()
            moves.append([line[0], int(line[1])])

    result = get_tail_positions(moves)

    print(result)
    #assert result == 36
    #print(f'DEMO Success for result: {result}')

    #assert result == None
    #print(f'Success for result: {result}')

if __name__ == "__main__":
    main()
