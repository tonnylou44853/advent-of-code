# Day 8 Challenge

import numpy as np
from math import prod

def visible_trees(data: np.ndarray, trees_coor: list):
    for i, d1 in enumerate(data[1:-1]):
        max_coor = (i+1, 0)
        for j, d2 in enumerate(d1[1:-1]):
            if d2 > data[max_coor]:
                if (i+1, j+1) not in trees_coor:
                    trees_coor.append((i+1, j+1))
                max_coor = (i+1, j+1)
                j += 1
    return trees_coor

def scenic_score(data: np.ndarray):
    score_mat = np.ones(shape=[len(data)-2, len(data)-2])
    for i, d1 in enumerate(data[1:-1]):
        for j, d2 in enumerate(d1[1:-1]):
            score = 0
            for d3 in d1[j+2:]:
                score += 1
                if d2 <= d3:
                    break
            score_mat[i, j] = score
    return score_mat

def main():
    data_path = './data/day8_input.txt'
    with open(data_path) as f:
        data = []
        for line in f.readlines():
            data.append(list(map(int, [*line.strip('\n')])))
    data = np.array(data)
    flip_len = data.shape[0] - 1

    fun = [
        [lambda lst: lst, lambda data: data],
        [lambda lst: [(l[0], flip_len-l[1]) for l in lst], lambda data: np.flip(data, 1)],
        [lambda lst: [l[::-1] for l in lst], lambda data: data.transpose()],
        [lambda lst: [(l[1], flip_len-l[0]) for l in lst], lambda data: np.flip(data, 0).transpose()]
    ]

    trees_coor = []
    score_mats = []
    for f in fun:
        trees_coor = f[0](visible_trees(data=f[1](data), trees_coor=f[0](trees_coor)))
        score_mats.append(f[1](scenic_score(data=f[1](data))))

    correction = lambda data: np.flip(data.transpose(), 0)
    score_mats[-1] = correction(correction(score_mats[-1]))

    print("Part 1:", len(trees_coor) + flip_len * 4)
    print("Part 2:", int(prod(score_mats).max()))

if __name__ == '__main__':
    main()