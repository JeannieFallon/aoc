import sys
import fileinput


def get_total_paper(presents: list):
    total = 0
    for present in presents:
        d = [int(i) for i in present.split('x')]

        side_1 = d[0]*d[1]
        side_2 = d[1]*d[2]
        side_3 = d[2]*d[0]

        slack = sorted([side_1, side_2, side_3])[0]

        total += 2*side_1 + 2*side_2 + 2*side_3 + slack

    return total


def main():
    presents = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            presents.append(line.strip())

    result = get_total_paper(presents)

    assert result == 1598415
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
