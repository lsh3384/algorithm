import sys

S = int(sys.stdin.readline())

N = 0
adder = 1
total = 0
difference = S - total
while difference > 0:
    total += adder
    adder += 1
    N += 1
    difference = S - total

if difference < 0:
    print(N - 1)
else:
    print(N)