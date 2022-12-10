# Day 1 Challenge

def main():
    data_path = './data/day1_input.txt'
    with open(data_path) as f:
        contents = [line.splitlines() for line in f.read().split('\n\n')]
        carlories_list = [sum(list(map(int, line))) for line in contents]
    print("Part 1:", max(carlories_list))
    top_n_carlories = 0
    for _ in range(3):
        top_n_carlories += max(carlories_list)
        carlories_list.remove(max(carlories_list))
    print("Part 2:", top_n_carlories)

if __name__=='__main__':
    main()