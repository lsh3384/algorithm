import sys

A, B = sys.stdin.readline().rstrip().split()

min_A = A.replace('6', '5')
min_B = B.replace('6', '5')

min_val = int(min_A) + int(min_B)

max_A = A.replace('5', '6')
max_B = B.replace('5', '6')

max_val = int(max_A) + int(max_B)

print(min_val, max_val)