# Day 10 Challenge

def main():
    data_path = './data/day10_input.txt'
    with open(data_path) as f:
        data = [line.strip('\n').split(' ') for line in f.readlines()]

    cycles = [1]
    for d in data:
        if d[0] == 'noop':
            temp = 0
        elif d[0] == 'addx':
            temp = int(d[1])
            cycles.append(cycles[-1])
        cycles.append(cycles[-1] + temp)

    sum_signal_strengths = (
        cycles[19] * 20 + cycles[59] * 60 + cycles[99] * 100
        + cycles[139] * 140 + cycles[179] * 180 + cycles[219] * 220)
    print("Part 1:", sum_signal_strengths)

    draw_line = ''
    print("Part 2:")
    for i, cycle in enumerate(cycles):
        draw_line += '#' if i % 40 in [cycle - 1, cycle, cycle + 1] else '.'
        if i % 40 == 39:
            print(draw_line)
            draw_line = ''

if __name__=='__main__':
    main()