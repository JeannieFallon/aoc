import sys
import fileinput

'''
python 10_2.py input_10.txt
'''


def get_signal_sum(inst: list):
    signal_sum = 0
    x_reg = 1
    queue = [0]

    #cycle = 1
    idx = cycle = 0
    #while idx < len(inst):
    #while inst:
    while len(queue):

        print(f'Start of cycle {cycle} with len(inst) {len(inst)}. Queue:\n{queue}')
        # Check signal strength every 20 cycles
        if cycle == 20 or not (20 + cycle) % 40:
            print(f'>>> check x ({x_reg}) at cycle {cycle}. signal strength is {cycle * x_reg}')
            signal_sum += cycle * x_reg

        curr_inst = inst.pop(0) if len(inst) else None
        print(f'Curr inst {curr_inst} on cycle {cycle}')
        if curr_inst:
            op, val = curr_inst[0], curr_inst[1]
        else:
            op, val = None, None
        #op, val = inst[idx][0], inst[idx][1]

        # Check queue for stored vals
        V = queue.pop(0) if len(queue) else None
        if V:
            print(f'adding value {V} to x {x_reg} at end of cycle {cycle}')
            x_reg += V
            idx += 1

        match op:
            case 'addx':
                # Store val to be added in two cycles
                queue.append(0)
                queue.append(val)
            case 'noop':
                queue.append(0)
                print(f'noop on cycle {cycle}')
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
