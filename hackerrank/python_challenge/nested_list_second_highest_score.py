if __name__ == '__main__':
    score_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_dict[score] = score_dict.get(score, []) + [name]
    unique_key_list = list(set(score_dict.keys()))
    unique_key_list.sort()
    score_dict[unique_key_list[1]].sort()
    # print(score_dict)
    for i in score_dict[unique_key_list[1]]:
        print(i)