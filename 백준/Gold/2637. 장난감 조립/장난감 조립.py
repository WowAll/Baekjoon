import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
indegree = [0] * (N + 1)
graph = [deque() for _ in range(N + 1)]
ans = []
unit = [[0] * (N + 1) for _ in range(N + 1)]

q = deque()

for i in range(M):
    X, Y, K = map(int, sys.stdin.readline().strip().split())
    indegree[X] += 1
    graph[Y].append((K, X))

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        unit[i][i] = 1
while q:
    cur = q.popleft()
    ans.append(cur)
    for next_cnt, next in graph[cur]:
        for i in range(1, N + 1):
            unit[next][i] += unit[cur][i] * next_cnt
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in range(1, N):
    if unit[N][i] > 0:
        print(i, unit[N][i])