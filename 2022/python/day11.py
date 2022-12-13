# Day 11 Challenge

from functools import partial
from math import prod
from copy import deepcopy

def create_monkeys(data: list):
    monkey_list = [{} for _ in range(len(data))]
    operation_map = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
    }
    for i, d in enumerate(data):
        monkey_list[i]['items'] = list(map(int, d[1].replace('  Starting items: ', '').split(', ')))
        operation = d[2].replace('  Operation: new = old ', '').split(' ')
        if operation[1] != 'old':
            monkey_list[i]['operation'] = partial(operation_map[operation[0]], y=int(operation[1]))
        else:
            monkey_list[i]['operation'] = lambda z: z * z
        monkey_list[i]['test'] = int(d[3].replace('  Test: divisible by ', ''))
        monkey_list[i][True] = int(d[4].replace('    If true: throw to monkey ', ''))
        monkey_list[i][False] = int(d[5].replace('    If false: throw to monkey ', ''))
        monkey_list[i]['inspections'] = 0
    return monkey_list

def monkey_business(monkey_list: list, rounds: int, worry_regulator: int):
    monkeys = deepcopy(monkey_list)
    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey['items'])):
                monkey['inspections'] += 1
                worry_level = int(monkey['operation'](monkey['items'][0]))
                worry_level = worry_level // worry_regulator
                condition = (worry_level % monkey['test'] == 0)
                if worry_regulator == 1:
                    worry_level = worry_level % 9699690
                monkeys[monkey[condition]]['items'].append(worry_level)
                monkey['items'].pop(0)
    return prod(sorted([monkey['inspections'] for monkey in monkeys], reverse=True)[:2])

def main():
    data_path = './data/day11_input.txt'
    with open(data_path) as f:
        data = [line.splitlines() for line in f.read().split('\n\n') ]
    monkeys = create_monkeys(data=data)

    print("Part 1:", monkey_business(monkey_list=monkeys, rounds=20, worry_regulator=3))
    print("Part 2:", monkey_business(monkey_list=monkeys, rounds=10000, worry_regulator=1))

if __name__=='__main__':
    main()