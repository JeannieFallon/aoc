import sys
import fileinput


class Direction:
    NORTH = '^'
    SOUTH = 'v'
    EAST = '>'
    WEST = '<'


def get_houses(directions: list):
    visit = [[0,0]]
    s_curr = visit[0].copy()
    r_curr = visit[0].copy()

    for idx, d in enumerate(directions):
        curr = s_curr if idx % 2 else r_curr
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
        if curr not in visit:
            visit.append(curr.copy())

    return len(visit)


def main():
    directions = ''
    with fileinput.input(encoding="utf-8") as f:
        directions = f.readline().strip()

    result = get_houses(directions)

    assert result == 2639
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
