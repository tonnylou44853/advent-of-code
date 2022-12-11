# Day 9 Challenge

def trace(data: list, n_knots: int):
    t_set = [[0, 0]]
    coor = [[0, 0] for _ in range(n_knots)]
    x_trans = {'R': 1, 'L': -1}
    y_trans = {'U': 1, 'D': -1}
    for d in data:
        for _ in range(int(d[1])):
            if d[0] in x_trans:
                coor[0][0] += x_trans[d[0]]
            else:
                coor[0][1] += y_trans[d[0]]
            for i in range(n_knots-1):
                diff = [h - t for h, t in zip(coor[i], coor[i+1])]
                if sum([z**2 for z in diff]) > 2:
                    coor[i+1][0] += int(diff[0] / abs(diff[0])) if diff[0] != 0 else 0
                    coor[i+1][1] += int(diff[1] / abs(diff[1])) if diff[1] != 0 else 0
            t_set.append(coor[-1].copy())
    return t_set

def main():
    data_path = './data/day9_input.txt'
    with open(data_path) as f:
        data = [line.strip('\n').split(' ') for line in f.readlines()]

    print("Part 1: ", len({tuple(l) for l in trace(data=data, n_knots=2)}))
    print("Part 2: ", len({tuple(l) for l in trace(data=data, n_knots=10)}))

if __name__=='__main__':
    main()