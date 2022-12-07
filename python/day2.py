# Day 2 Challenge

def convert_data(data_path: str):
    replacements = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    with open(data_path) as f:
        extracted_data = [line.strip('\n').split() for line in f.readlines()]
    converted_data = [[replacements[data[0]], replacements[data[1]]] for data in extracted_data]
    return converted_data

def scores(matches: list):
    convert_to_match_score = [3, 0, 6]
    base_score = 0
    match_score = 0
    for player in matches:
        base_score += player[-1]
        match_score += convert_to_match_score[player[0] - player[1]]
    return match_score + base_score

def corrected_scores(matches: list):
    convert_base_score = [1, 2, 3]
    convert_match_score = {1: 0, 2: 3, 3: 6}
    base_score = 0
    match_score = 0
    for player in matches:
        match_score += convert_match_score[player[1]]
        base_score += convert_base_score[sum(player)%3]
    return match_score + base_score

def main():
    data_path = './data/day2_input.txt'
    data = convert_data(data_path=data_path)
    print('Part 1 score is:', scores(matches=data))
    print('Part 2 score is:', corrected_scores(matches=data))
    return None

if __name__=='__main__':
    main()