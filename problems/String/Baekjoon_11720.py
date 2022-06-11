import sys

N = int(sys.stdin.readline().rstrip())

S = sys.stdin.readline().rstrip()
S_list = [int(c) for c in S]
print(sum(list(S_list)))