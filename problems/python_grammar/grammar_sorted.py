example_dict = {3: 1, 2: 2, 1: 3}

# 딕셔너리의 key를 기준으로 오름차순으로 정렬하기
print(sorted(example_dict.items(), key= lambda x: x[0]))

# 딕셔너리의 value를 기준으로 오름차순으로 정렬하기
print(sorted(example_dict.items(), key= lambda x: x[1]))

# 딕셔너리의 key를 기준으로 내림차순으로 정렬하기
print(sorted(example_dict.items(), key= lambda x: x[0], reverse=True))

# 딕셔너리의 value를 기준으로 내림차순으로 정렬하기
print(sorted(example_dict.items(), key= lambda x: x[1], reverse=True))