import re
import sys
import fileinput

'''
python 03_2.py input_01.txt
'''

def get_product(mul: str) -> int:
    x, y = mul.split(",")
    x = int(re.sub(r"\D", "", x))
    y = int(re.sub(r"\D", "", y))

    return x * y


def get_uncorrupted_sum(corrupted: list) -> int:
    sum = 0
    enabled = True
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)"

    for line in corrupted:
        hits = re.findall(pattern, line)

        for hit in hits:
            stub = hit[:3]
            if stub == 'mul':
                if enabled:
                    sum += get_product(hit)
            else:
                enabled = False if stub == 'don' else True

    return sum


def main() -> int:
    corrupt = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            corrupt.append(line)

    result = get_uncorrupted_sum(corrupt)

    print(f'Success for result: {result}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
