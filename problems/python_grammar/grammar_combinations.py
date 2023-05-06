from itertools import combinations

arr = ['A', 'B', 'C']
nCr = combinations(arr, 2)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]