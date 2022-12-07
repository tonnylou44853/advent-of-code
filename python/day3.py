# Day 3 Challenge

from functools import reduce

def read_data(data_path: str):
    with open(data_path) as f:
        extracted_data = [line.strip('\n') for line in f.readlines()]
    return extracted_data

def find_common_item_part1(data: list):
    splitted_data = [[d[:int(len(d)/2)], d[int(len(d)/2):]] for d in data]
    common_item = []
    for data in splitted_data:
        common_item.append(list(reduce(lambda i, j: i & j, (set(x) for x in data))))
    return [item for items in common_item for item in items]

def find_common_item_part2(data: list):
    splitted_data = list(zip(*[iter(data)]*3))
    common_item = []
    for data in splitted_data:
        common_item.append(list(reduce(lambda i, j: i & j, (set(x) for x in data))))
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
    data = read_data(data_path=data_path)
    common_item_part1 = find_common_item_part1(data=data) 
    common_item_part2 = find_common_item_part2(data=data)  
    priorities1 = assign_priorities(common_item_part1)
    priorities2 = assign_priorities(common_item_part2)
    print("Part 1: ", sum(priorities1))
    print("Part 2: ", sum(priorities2))

if __name__ == '__main__':
    main()