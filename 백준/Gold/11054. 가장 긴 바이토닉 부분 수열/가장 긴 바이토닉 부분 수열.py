import sys
from collections import deque

INF = 2 ** 31 - 1

N = int(sys.stdin.readline().strip())

stack = [[] for _ in range(N)]

dp_l = [1] * N
dp_g = [1] * N

num = list(map(int, sys.stdin.readline().strip().split()))

idx = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if num[i] < num[j]:
            dp_l[j] = max(dp_l[j], dp_l[i] + 1)

for i in range(N - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if num[i] < num[j]:
            dp_g[j] = max(dp_g[j], dp_g[i] + 1)

ans = 0

for i in range(N):
    ans = max(ans, dp_g[i] + dp_l[i])
print(ans - 1)