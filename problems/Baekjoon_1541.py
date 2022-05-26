equation = input()

A = list(equation.split('-'))

B = []
for i in A:
    B.append(sum(map(int, i.split('+'))))

total = int(B.pop(0))
for i in B:
    total -= i

print(total)
