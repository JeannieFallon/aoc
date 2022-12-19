import sys
import fileinput

'''
python 12_1.py input_12.txt
'''

START = 'S'
END = 'E'


def walk_grid(grid: list):
    '''Transform alpha vals to ints and find S & E'''
    S = []
    E = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == START:
                S.append(i)
                S.append(j)
                continue
            if grid[i][j] == END:
                E.append(i)
                E.append(j)
                continue
            grid[i][j] = ord(grid[i][j])

    return grid, S, E


def get_moves(grid: list, curr: list):
    moves = {'L':[],'R':[],'U':[],'D':[]}
    max_col_idx = len(grid[0]) - 1
    max_row_idx = len(grid) - 1

    L_y = curr[1] - 1
    R_y = curr[1] + 1
    U_x = curr[0] - 1
    D_x = curr[0] + 1

    moves['L'] = [curr[0], L_y] if L_y > 0 else [None, None]
    moves['R'] = [curr[0], R_y] if R_y < max_col_idx else [None, None]
    moves['U'] = [U_x, curr[1]] if U_x > 0 else [None, None]
    moves['D'] = [D_x, curr[1]] if D_x < max_row_idx else [None, None]

    return moves

def get_path(num_steps: int, grid: list, curr: list, previous_moves: list, available_moves: list, E: list):
    print(f'>>> start get_path for curr: {curr}')

    if not len(available_moves):
        # Dead end path
        return -1, curr

    curr_val = grid[curr[0]][curr[1]]
    if curr_val == 'E':
        # Reached destination
        return num_steps, curr
    if curr_val == 'S':
        # Special case for starting block
        curr_val = 97

    num_steps += 1

    print(f'available_moves {available_moves}')
    print(f'previous_moves: {previous_moves}')
    '''
    for move in available_moves:
        # Move is new current, current is now in previous
        num_steps, curr = get_path(num_steps, grid, move, previous_moves, available_moves, E)

    return num_steps, curr
    '''

    #return get_path(num_steps, grid, curr, previous_moves, available_moves, E)
    return num_steps, curr

def get_fewest_steps(grid: list):
    paths = []      # list of possible paths by step count
    curr = [0,0]    # X,Y of current position in grid
    moves = {}      # left/right/up/down for curr position

    grid, S, E = walk_grid(grid)

    # Set current position to start location
    curr[0] = S[0]
    curr[1] = S[1]
    previous_moves = []
    while curr[0] != E[0] and curr[1] != E[1]:
        curr_val = grid[curr[0]][curr[1]]
        # FIXME gross
        if curr_val == 'S':
            curr_val = 97

        # Get left/right/up/down positions as possible moves
        moves = get_moves(grid, curr)

        # Check which moves fit elevation rules, and disregard previous location
        available_moves = []
        for k, v in moves.items():
            if v[0] is None:
                continue
            #print(f'v: {v}')
            if v in previous_moves:
                #print('!!!!!! found previous move {v}')
                continue
            move_val = grid[v[0]][v[1]]
            if move_val <= curr_val or move_val - curr_val == 1:
                #print(f'add move {k},{v}')
                available_moves.append([v[0],v[1]])

        previous_moves.append(curr)

        # Init recursive walk
        num_steps = 0
        for move in available_moves:
            num_steps, curr = get_path(num_steps, grid, move, previous_moves, available_moves, E)

        paths.append(num_steps)

    fewest_steps = sorted(paths)[0]

    return fewest_steps


def main():
    grid = []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            grid.append(list(line.strip()))

    result = get_fewest_steps(grid)

    print(result)
    #assert result == 31
    #print(f'DEMO Success for result: {result}')
    #assert result == None
    #print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
