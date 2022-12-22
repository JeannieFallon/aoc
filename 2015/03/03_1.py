import sys
import fileinput


class Direction:
    NORTH = '^'
    SOUTH = 'v'
    EAST = '>'
    WEST = '<'


def get_houses(directions: list):
    visited = [[0,0]]
    curr = visited[0].copy()

    for d in directions:
        match d:
            case Direction.NORTH:
                ''' x - 1 '''
                curr[0] -= 1
            case Direction.SOUTH:
                ''' x + 1 '''
                curr[0] += 1
            case Direction.EAST:
                ''' y - 1 '''
                curr[1] -= 1
            case Direction.WEST:
                ''' y +  1 '''
                curr[1] += 1
            case _:
                raise ValueError(f"Unknown direction: {d}")
        if curr not in visited:
            visited.append(curr.copy())

    return len(visited)


def main():
    directions = ''
    with fileinput.input(encoding="utf-8") as f:
        directions = f.readline().strip()

    result = get_houses(directions)

    assert result == 2565
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
