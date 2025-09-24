import sys
from collections import deque

INF = 2 ** 31 - 1

N, M = map(int, sys.stdin.readline().strip().split())

ans = 0

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    heavy, light = map(int, sys.stdin.readline().strip().split())
    graph[heavy][light] = 1

for k in range(1, N + 1):
    for j in range(1, N + 1):
        for i in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, N + 1):
    heavier = 0
    lighter = 0
    for j in range(1, N + 1):
        if graph[i][j] == 1:
            lighter += 1
        if graph[j][i] == 1:
            heavier += 1
    if heavier > (N // 2) or lighter > (N // 2):
        ans += 1
print(ans)