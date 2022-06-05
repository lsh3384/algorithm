import sys

S = sys.stdin.readline().rstrip()

s_dict = {'0': 0, '1': 0}

continued = 'x'

for i in range(len(S)):
    if S[i] != continued:
        s_dict[S[i]] += 1
        continued = S[i]
    else:
        pass

result = sorted(s_dict.items(), key=lambda x: x[1])
print(result[0][1])