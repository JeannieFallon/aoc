import sys
import fileinput

'''
python 02_1.py input_01.txt
'''

def get_safe_reports(reports: list) -> int:
    safe_reports = 0

    '''
    Report is safe if:
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    '''

    for report in reports:
        is_increase = False
        is_safe = False
        for i in range(len(report[:-1])):
            curr = int(report[i])
            next = int(report[i+1])
            if curr == next:
                break
            elif abs(curr - next) > 3:
                break
            elif curr > next:
                if i > 0 and is_increase:
                    break
            elif curr < next:
                if i > 0 and not is_increase:
                    break
                is_increase = True

            # Have we made it to the penultimate value?
            if i == len(report) - 2:
                is_safe = True

        safe_reports += 1 if is_safe else 0

    return safe_reports


def main() -> int:
    reports = []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            vals = line.split()
            reports.append(vals)

    result = get_safe_reports(reports)

    '''
    # Demo
    assert result == 2
    '''
    print(f'Success for result: {result}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
