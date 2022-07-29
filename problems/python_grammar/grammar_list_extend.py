# 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다.
# iterable의 항목들이 들어온다고 보면 된다.

x = ['one', 'two', 'three']
y = ['four', 'five']

x.extend(y)
print(x)
# 결과 ['one', 'two', 'three', 'four', 'five']

# append와 비교해서 알아두자.
a = ['one', 'two', 'three']
b = ['four', 'five']
a.append(b)
print(a)

# 결과 ['one', 'two', 'three', ['four', 'five']]