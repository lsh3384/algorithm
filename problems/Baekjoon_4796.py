import sys

i = 1
camping = []

while True:
    L, P, V = (map(int, sys.stdin.readline().split()))
    if ( L == 0 and P == 0 and V == 0):
        break
    camping.append((L, P, V))

for i in range(len(camping)):
    result = ((camping[i][2] // camping[i][1]) * camping[i][0]) + min((camping[i][2] % camping[i][1]), camping[i][0])
    print('Case ' + str(i+1) + ': ' + str(result))