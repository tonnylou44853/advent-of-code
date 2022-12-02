# Day 1 Challenge

def elf_carlories(data_path: str):
    carlories_list = []
    carlories = 0
    with open(data_path) as f:
        contents = [line.strip('\n') for line in f.readlines()]
        for line in contents:
            if line == '':
                carlories_list.append(carlories)
                carlories = 0
            else:
                carlories += int(line)
    return carlories_list

def find_top_elf(carlories_list: list):
    indices = [index for index, item in enumerate(carlories_list) if item == max(carlories_list)]
    return indices, max(carlories_list)

def find_top_n_elf(n: int, carlories_list: list):
    top_n_carlories = []
    indices = []
    for _ in range(n):
        indices = indices + [index for index, item in enumerate(carlories_list) if item == max(carlories_list)]
        top_n_carlories.append(max(carlories_list))
        carlories_list.pop(indices[-1])
    return indices, top_n_carlories


def main():
    data_path = './data/day1_input.txt'
    n = 3
    carlories_list = elf_carlories(data_path=data_path)
    index, val = find_top_elf(carlories_list=carlories_list)
    print('The', index, 'Elf is carrying the most Calories:', val)
    indices, vals = find_top_n_elf(n=n, carlories_list=carlories_list)
    print('The top', n, 'elves are:', indices, 'with total carlories:', vals, 'respectively.')
    print('The total carlories of the', n, 'elves is:', sum(vals))
    return None

if __name__=='__main__':
    main()