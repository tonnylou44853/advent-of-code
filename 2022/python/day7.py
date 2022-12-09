# Day 7 Challenge

from copy import copy

def items_in_folder(data: list):
    items = []
    data = [d.split(' ') for d in data]
    for d in data:
        if d[0] == 'dir':
            items.append({'name': d[1], 'size': 0, 'content': []})
        else:
            items.append({'name': d[1], 'size': int(d[0]), 'content': None})
    return items

def assign_items(file_system: dict, path: list, items: list, idx: int):
    lst = copy(path)
    for file in file_system:
        if file['content'] != None and file['name'] == lst[idx]:
            if (idx + 1) < len(lst):
                idx += 1
                assign_items(file['content'], lst, items, idx)
            else:
                file['content'] = items

def assign_sizes(file_system: list, sizes: int):
    temp = 0
    for file in file_system:
        if file['content'] != None:
            file['size'] = assign_sizes(file['content'], sizes)
        temp += file['size']
    return temp

def total_sizes(file_system: list, threshold: int, upper_bound: bool):
    total_size = 0
    lst = []
    for file in file_system:
        if file['content'] != None:
            condition = file['size'] > threshold
            if upper_bound ^ condition:
                lst.append(file)
                total_size += file['size']
            t, l = total_sizes(file['content'], threshold, upper_bound)
            total_size += t
            lst = lst + l
    return total_size, lst

def main():
    data_path = './data/day7_input.txt'
    file_system = [{'name': '/', 'size': 0, 'content': []}]
    with open(data_path) as f:
        commands, temp = [], []
        for line in f.readlines(): 
            if line[0] == '$':
                commands.append(temp)
                temp = []
            temp.append(line.strip('\n'))
        commands.append(temp)
        commands.pop(0)

    path = []
    for command in commands:
        if '$ cd ' in command[0]:
            folder_name = command[0].replace('$ cd ', '')
            if '..' in command[0]:
                path.pop(-1)
            else:
                path.append(folder_name)
        if '$ ls' in command[0]:
            items = items_in_folder(command[1:])
            assign_items(file_system=file_system, path=path, items=items, idx=0)
    assign_sizes(file_system=file_system, sizes=0)

    print("Part 1:", total_sizes(file_system=file_system, threshold=100000, upper_bound=True)[0])

    _, lst = total_sizes(file_system=file_system, threshold=file_system[0]['size']-40000000, upper_bound=False)
    
    print("Part 2:", sorted(lst, key=lambda x: x['size'])[0]['size'])

if __name__ == '__main__':
    main()