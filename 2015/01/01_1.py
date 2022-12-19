import sys
import fileinput

class Directions:
    UP = '('
    DOWN = ')'

def get_target_floor(directions: str):
    floor = 0
    for c in directions:
        match c:
            case Directions.UP:
                floor += 1
            case Directions.DOWN:
                floor -= 1
            case _:
                raise ValueError(f'Invalid direction: {c}')
    return floor


def main():
    directions = ''
    with fileinput.input(encoding="utf-8") as f:
        directions = f.readline().strip()
    result = get_target_floor(directions)

    assert result == 74
    print(f'Success for result: {result}')

if __name__ == "__main__":
    main()
