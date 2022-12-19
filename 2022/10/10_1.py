import sys
import fileinput

'''
python 10_1.py input_10.txt
'''


def get_signal_sum(inst: list):
    signal_sum = 0
    x_reg = 1
    queue = [0]

    idx = cycle = 0
    while len(queue):
        # Check signal strength every 20 cycles
        if cycle == 20 or not (20 + cycle) % 40:
            signal_sum += cycle * x_reg

        curr_inst = inst.pop(0) if len(inst) else None
        if curr_inst:
            op, val = curr_inst[0], curr_inst[1]
        else:
            op, val = None, None

        # Check queue for stored vals
        V = queue.pop(0) if len(queue) else None
        if V:
            x_reg += V
            idx += 1

        match op:
            case 'addx':
                # Store val to be added in two cycles
                queue.append(0)
                queue.append(val)
            case 'noop':
                queue.append(0)
            case None:
                pass
            case _:
                raise ValueError('Instruction not implemented')

        cycle += 1

    return signal_sum


def main():
    inst = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            line = line.split()
            inst.append([line[0], int(line[1]) if len(line) > 1 else None])

    result = get_signal_sum(inst)

    assert result == 14360
    print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
