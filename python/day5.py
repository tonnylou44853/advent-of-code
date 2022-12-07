# Day 5 Challenge

from copy import copy

def moves_and_stacks(data_path: str):
    with open(data_path) as f:
        moves = []
        temp_stacks = []
        for line in f.readlines(): 
            if line[:4] == 'move':
                moves.append(list(map(int, line.strip('\n').replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))))
            elif line[0] != '\n':
                temp_stacks.append(line.strip('\n').replace('[', '').replace(']', '').replace('  ', ' '))
    stacks = [''] * int(temp_stacks[-1].strip(' ')[-1])
    temp_stacks.pop(-1)
    temp_stacks = [list(map(''.join, zip(*[iter(s + ' ')]*2))) for s in temp_stacks]

    for _, stack in enumerate(temp_stacks[::-1]):
        count = 0
        for element in stack:
            if element != '  ':
                stacks[count] = stacks[count] + element.strip(' ')
            count += 1
    
    return moves, stacks

def main():
    data_path = './data/day5_input.txt'
    moves, stacks = moves_and_stacks(data_path=data_path)    

    part1_stacks = copy(stacks)
    part2_stacks = copy(stacks)
    
    for move in moves:
        part1_stacks[move[2]-1] = part1_stacks[move[2]-1] + part1_stacks[move[1]-1][-move[0]:][::-1]
        part1_stacks[move[1]-1] = part1_stacks[move[1]-1][:-move[0]]
        part2_stacks[move[2]-1] = part2_stacks[move[2]-1] + part2_stacks[move[1]-1][-move[0]:]
        part2_stacks[move[1]-1] = part2_stacks[move[1]-1][:-move[0]]

    print("Part 1: ", [stack[-1] for stack in part1_stacks])
    print("Part 2: ", [stack[-1] for stack in part2_stacks])

if __name__ == '__main__':
    main()