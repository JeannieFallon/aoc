import sys
import fileinput


def get_total_ribbon(presents: list):
    total = 0
    for present in presents:
        d = sorted([int(i) for i in present.split('x')])
        total += (2*d[0] + 2*d[1]) + d[0]*d[1]*d[2]
    return total


def main():
    presents = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            presents.append(line.strip())

    result = get_total_ribbon(presents)

    assert result == 3812909
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
