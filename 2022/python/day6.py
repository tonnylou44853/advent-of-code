# Day 6 Challenge

def marker(data_path: str, number_of_char):
    with open(data_path) as f:
        data = f.readlines()[0]
    for i, d in enumerate(data[number_of_char-1:]):
        joint_data = data[i:i+number_of_char-1]
        if d not in joint_data and len(set(joint_data)) == number_of_char - 1:
            return i + number_of_char

def main():
    data_path = './data/day6_input.txt'
    print("Part 1: ", marker(data_path=data_path, number_of_char=4))
    print("Part 2: ", marker(data_path=data_path, number_of_char=14))

if __name__ == '__main__':
    main()
