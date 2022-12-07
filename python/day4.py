# Day 4 Challenge

def count_overlap(data: list):
    full_overlaps = 0
    no_overlaps = 0
    for d1, d2 in zip(data[::2], data[1::2]):
        if (d1[0] <= d2[0] and d1[1] >= d2[1]) or (d1[0] >= d2[0] and d1[1] <= d2[1]):
            full_overlaps += 1
        elif (d1[1] < d2[0] and d1[0] < d2[1]) or (d1[0] > d2[1] and d1[1] > d2[0]):
            no_overlaps += 1
    return full_overlaps, (len(data[::2]) - no_overlaps)

def main():
    data_path = './data/day4_input.txt'
    with open(data_path) as f:
        data = [list(map(int, l.split('-'))) for line in f.readlines() for l in line.strip('\n').split(',')]
    print("Part 1: {}, Part 2: {}".format(*count_overlap(data=data)))

if __name__ == '__main__':
    main()