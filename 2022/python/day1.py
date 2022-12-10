# Day 1 Challenge

def main():
    data_path = './data/day1_input.txt'
    with open(data_path) as f:
        contents = [line.splitlines() for line in f.read().split('\n\n')]
    carlories_list = [sum(list(map(int, line))) for line in contents]
    carlories_list.sort(reverse=True)
    print("Part 1:", carlories_list[0])
    print("Part 2:", sum(carlories_list[:3]))

if __name__=='__main__':
    main()