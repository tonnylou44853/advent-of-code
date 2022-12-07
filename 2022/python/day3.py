# Day 3 Challenge

from functools import reduce

def find_common_item(data: list):
    common_item = []
    for d in data:
        common_item.append(list(reduce(lambda i, j: i & j, (set(x) for x in d))))
    return [item for items in common_item for item in items]

def assign_priorities(data: list):
    priorities = []
    for d in data:
        if d.isupper():
            priorities.append(ord(d) - 38)
        else:
            priorities.append(ord(d) - 96)
    return priorities

def main():
    data_path = './data/day3_input.txt'
    with open(data_path) as f:
        data = [line.strip('\n') for line in f.readlines()]
    part1_data = [[d[:int(len(d)/2)], d[int(len(d)/2):]] for d in data]
    priorities1 = assign_priorities(find_common_item(data=part1_data))
    print("Part 1: ", sum(priorities1))
    part2_data = list(zip(*[iter(data)]*3))
    priorities2 = assign_priorities(find_common_item(data=part2_data))
    print("Part 2: ", sum(priorities2))

if __name__ == '__main__':
    main()