import sys
import fileinput

class Directions:
    UP = '('
    DOWN = ')'

def get_target_floor(directions: str):
    floor = 0
    for idx, c in enumerate(directions):
        match c:
            case Directions.UP:
                floor += 1
            case Directions.DOWN:
                floor -= 1
            case _:
                raise ValueError(f'Invalid direction: {c}')
        if floor == -1:
            return idx + 1



def main():
    directions = ''
    with fileinput.input(encoding="utf-8") as f:
        directions = f.readline().strip()
    result = get_target_floor(directions)

    assert result == 1795
    print(f'Success for result: {result}')

if __name__ == "__main__":
    main()
