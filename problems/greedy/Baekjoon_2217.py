
import sys

def solution():
    arr.sort(reverse=True)
    for i in range(N):
        arr[i] = arr[i] * (i + 1)
 
    return max(arr)
 
 
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
 
print(solution())