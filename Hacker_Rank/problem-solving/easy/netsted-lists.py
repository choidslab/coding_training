if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    # records = sorted(records, key=lambda x: x[0])
    score_list = []

    for record in records:
        score_list.append(record[1])

    # find out second-lowest score
    second_lowest_score = sorted(list(set(score_list)))[1]

    # sorting order by name
    records = sorted(records, key=lambda x: x[0])

    # print name
    for record in records:
        if record[1] == second_lowest_score:
            print(record[0])
