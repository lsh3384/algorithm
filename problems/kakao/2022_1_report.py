def solution(id_list, report, k):
    dict_report = {}
    for i in id_list:
        dict_report[i] = set()

    for j in report:
        a, b = j.split()
        dict_report[b].add(a);

    answer = [0 for _ in range(len(id_list))]

    for k, v in dict_report.items():
        if len(v) >= 2:
            for name in v:
                answer[id_list.index(name)] += 1

    print(answer)

    return answer