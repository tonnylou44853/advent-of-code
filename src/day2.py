# Day 2 Challenge

def extract_data(data_path: str):
    with open(data_path) as f:
        rounds = [line.strip('\n').split() for line in f.readlines()]
    return rounds

def scores(data_path: str):
    replacements = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    convert_to_score = [3, 0, 6]
    base_score = 0
    rounds = extract_data(data_path=data_path)
    for i, player in enumerate(rounds):
        rounds[i] = [replacements[player[0]], replacements[player[1]]]
        base_score += rounds[i][-1]
    diff = [convert_to_score[player[0] - player[1]] for player in rounds]
    match_score = sum(diff)
    return match_score + base_score

def corrected_scores(data_path: str):
    replacements = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    convert_base_score = [1, 2, 3]
    convert_match_score = {'X': 0, 'Y': 3, 'Z': 6}
    base_score = 0
    match_score = 0
    rounds = extract_data(data_path=data_path)
    for i, player in enumerate(rounds):
        match_score += convert_match_score[player[1]]
        rounds[i] = [replacements[player[0]], replacements[player[1]]]
        base_score += convert_base_score[sum(rounds[i])%3]
    return match_score + base_score

def main():
    data_path = './data/day2_input.txt'
    print('Part 1 score is:', scores(data_path=data_path))
    print('Part 2 score is:', corrected_scores(data_path=data_path))
    return None

if __name__=='__main__':
    main()