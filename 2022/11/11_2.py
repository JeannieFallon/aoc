import sys
import fileinput
from dataclasses import dataclass

'''
python 11_2.py input_11.txt
'''

@dataclass
class Monkey:
    items: list         # worry level for each item
    op: tuple           # new = old [0] [1]
    test: list          # divisible by [0], if true [1], if false [2]
    items_insp: int = 0   # number of items inspected

    def receive_item(self, item: int):
        self.items.append(item)

    def do_operation(self, old: int):
        new = 0
        val = int(self.op[1]) if self.op[1].isnumeric() else old
        match self.op[0]:
            case '*':
                new = old * val
            case '/':
                new = old / val
            case '+':
                new = old + val
            case '-':
                new = old - val
            case _:
                raise ValueError(f'Operater {self.op[0]} not implemented')
        return new

    def do_test(self, monkeys: list, item: int):
        if not item % self.test[0]:
            monkeys[self.test[1]].receive_item(item)
        else:
            monkeys[self.test[2]].receive_item(item)



def get_monkeys(lines: list, monkeys: list):
    for idx in range(0, len(lines), 7):
        items = [int(i.strip(',')) for i in lines[idx+1].split()[2:]]
        op = lines[idx+2].split()[-2:]
        test_val = int(lines[idx+3].split().pop())
        true_val = int(lines[idx+4].split().pop())
        false_val = int(lines[idx+5].split().pop())

        monkeys.append(Monkey(items, op, [test_val, true_val, false_val]))

    return monkeys


def get_level_of_monkey_business(monkeys: list):
    print(monkeys)
    level = 0
    for i in range(10000):
        for monkey in monkeys:
            #print(f'monkey items: {monkey.items}')
            for idx, item in enumerate(monkey.items):
                new = monkey.do_operation(item)
                monkey.do_test(monkeys, new)
                monkey.items_insp += 1
            # Clear monkey's item list after all have been inspected
            monkey.items = []
    '''
        print(f'\n>>> monkeys after round 1')
        for monkey in monkeys:
            print(monkey)
        return 0
    '''

    total_items = []
    for monkey in monkeys:
        total_items.append(monkey.items_insp)

    total_items.sort(reverse=True)
    print(total_items)
    level = total_items[0] * total_items[1]

    return level


def main():
    monkeys = []

    lines = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    monkeys = get_monkeys(lines, monkeys)
    result = get_level_of_monkey_business(monkeys)

    print(result)
    #assert result == 10605
    #print(f'DEMO Success for result: {result}')
    #assert result == 14360
    #print(f'Success for result: {result}')



if __name__ == "__main__":
    main()
