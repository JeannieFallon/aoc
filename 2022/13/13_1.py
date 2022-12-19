import ast
import sys
import fileinput

'''
python 13_1.py input_13.txt
'''

def get_packets(lines: list):
    packets = []
    for i in range(0, len(lines), 3):
        packet1 = ast.literal_eval(lines[i])
        packet2 = ast.literal_eval(lines[i+1])
        packets.append([packet1, packet2])

    return packets

def check_order(left: list, right: list):

    for idx, l in enumerate(left):
        print()
        print(f'left index is {idx}')
        print(f'left:{left}')
        print(f'right:{right}')

        if left and not right:
            return False

        # Left element is INT
        if isinstance(left[idx], int):
            print('left is int')
            # Right ran out of elements
            if len(left) > len(right):
                return False

            # Right is INT
            if isinstance(right[idx], int):
                print('> right[idx] is int')
                if left[idx] > right[idx]:
                    return False
            # Right is LIST
            if isinstance(right[idx], list):
                print('> right[idx] is list')
                if idx >= len(right) or not len(right[idx]):
                    return False
                if len(left) > len(right):
                    return False
                left_list = [left[idx]]
                return check_order(left_list, right[idx])

        # Left element is LIST
        elif isinstance(left[idx], list):
            print('left is list')
            # Right is INT
            if isinstance(right[idx], int):
                print('> right[idx] is int')
                right_list = [right[idx]]
                return check_order(left[idx], right_list)
            # Right is LIST
            if isinstance(right[idx], list):
                print('> right[idx] is list')
                if idx >= len(right) or not len(right[idx]):
                    return False
                if len(left) > len(right):
                    return False
                return check_order(left[idx], right[idx])

    return True


def get_indices_sum(packets: list):
    sum = 0

    for idx, pair in enumerate(packets):
        print(f'\n>>>> pair_idx: {idx+1}')
        left = pair[0]
        right = pair[1]

        foo = check_order(left, right)
        print(f'>>>> pair RESULT: {foo}')
        if foo:
        #if check_order(left, right):
            sum += idx + 1

    return sum

def main():
    lines = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    packets = get_packets(lines)
    result = get_indices_sum(packets)

    print(result)
    #assert result == 13
    #print(f'DEMO Success for result: {result}')
    #print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
