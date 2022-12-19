import sys
import fileinput

'''
python 06_2.py input_06.txt
'''

def find_marker(buff: str):
    marker = 0

    step = 14
    for i in range(0, len(buff)):
        if len(set(buff[i:i+step])) == step:
            marker = i + step
            break

    return marker


def main():
    buff = ''
    with fileinput.input(encoding="utf-8") as f:
        buff = f.readline()

    result = find_marker(buff)

    assert result == 2193
    print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
