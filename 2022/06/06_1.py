import sys
import fileinput

'''
python 06_1.py input_06.txt
'''

def find_marker(buff: str):
    marker = 0

    step = 4
    for i in range(0, len(buff), step):
        if len(set(buff[i:i+step])) == step:
            marker = i + step - 1
            break

    return marker


def main():
    buff = ''
    with fileinput.input(encoding="utf-8") as f:
        buff = f.readline()

    result = find_marker(buff)

    assert result == 1343
    print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
