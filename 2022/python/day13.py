# Day 13 Challenge

import ast
from pathlib import Path

INPUT_FILE = Path(
    Path(__file__).parent.parent, 
    f"data/{Path(__file__).stem}_input.txt"
)

def check_order(data1, data2, npair, order):
    for d1, d2 in zip(data1, data2):
        if isinstance(d1, int) and isinstance(d2, int):
            if d1 != d2: 
                order[npair] = (d1 < d2)
                break
        else:
            d1 = [d1] if isinstance(d1, int) else d1
            d2 = [d2] if isinstance(d2, int) else d2
            check_order(d1, d2, npair, order)
            if npair in order:
                break
    else:
        if len(data1) != len(data2):
            order[npair] = (len(data1) < len(data2))

def main():
    data_path = INPUT_FILE
    data = []
    with open(data_path) as f:
        data = [ast.literal_eval(line) for line in f.read().split('\n') if line != '']
    convert_to_list = lambda order: [a for a, b in order.items() if b]

    part1_data = [[d1, d2] for d1, d2 in zip(data[::2], data[1::2])]
    part1_order = {}
    for i, d in enumerate(part1_data):
        check_order(d[0], d[1], i+1, part1_order)
    print("Part 1:", sum(convert_to_list(part1_order)))

    part2_data = data.copy()
    part2_order1 = {}
    part2_order2 = {}
    for i, d in enumerate(part2_data):
        check_order(d, [[2]], i+1, part2_order1)
        check_order(d, [[6]], i+1, part2_order2)
    decoder_key = ((len(convert_to_list(part2_order1)) + 1)
                    * (len(convert_to_list(part2_order2)) + 2))
    print("Part 2:", decoder_key)

if __name__=='__main__':
    main()