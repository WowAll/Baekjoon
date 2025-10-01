import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
parent = [-1] * N

for i in range(N):
    for j in range(i):
        if num[j] < num[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            parent[i] = j


length = max(dp)

idx = dp.index(length)

lis = []
while idx != -1:
    lis.append(num[idx])
    idx = parent[idx]

lis.reverse()

print(length)
print(*lis)