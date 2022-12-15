# Day 12 Challenge

def bfs(height_map: list, end_location: tuple):
    width = len(height_map[0])
    height = len(height_map)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    new_pos = [0, 0]
    visited = {end_location: 0}
    queue = [list(end_location)]
    while queue:
        s = queue.pop(0)
        for direction in directions:
            new_pos[0] = s[0] + direction[0]
            new_pos[1] = s[1] + direction[1]
            limit_condition = (new_pos[0] < height and new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[1] < width)
            contain_condition = tuple(new_pos) not in visited
            if limit_condition and contain_condition:
                diff = height_map[s[0]][s[1]] - height_map[new_pos[0]][new_pos[1]]
                if diff <= 1:
                    visited[tuple(new_pos)] = visited[tuple(s)] + 1
                    queue.append(new_pos.copy())
    return visited

def main():
    data_path = './data/day12_input.txt'
    with open(data_path) as f:
        data = [line.strip('\n') for line in f.readlines()]
    height_map = []
    a_locations = []
    for i, line in enumerate(data):
        h = []
        for j, char in enumerate(line):
            h.append(ord(char) - 97)
            if char == 'S':
                start_location = (i, j)
                h[-1] = 0
                a_locations.append((i, j))
            elif char == 'E':
                end_location = (i, j)
                h[-1] = 25
            elif char == 'a':
                a_locations.append((i, j))
        height_map.append(h)
    
    visited = bfs(height_map=height_map, end_location=end_location)

    print("Part 1:", visited[start_location])
    print("Part 2:", min([visited.get(pos) for pos in a_locations if visited.get(pos) is not None]))

if __name__=='__main__':
    main()