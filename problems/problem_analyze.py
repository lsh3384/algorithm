

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

def solution(id_list, report, k):
    dict_report = {}
    for i in id_list:
        dict_report[i] = set()

    for j in report:
        a, b = j.split()
        dict_report[b].add(a)

    answer = [0 for _ in range(len(id_list))]

    for v in dict_report.values():
        if len(v) >= k:
            for name in v:
                answer[id_list.index(name)] += 1
    return answer

print(solution(id_list, report, k))
