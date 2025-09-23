import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
ans = []

q = deque()

for i in range(K):
    A, B = map(int, sys.stdin.readline().strip().split())
    indegree[B] += 1
    graph[A].append(B)

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
while q:
    cur = q.popleft()
    ans.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in ans:
    print(i, end=' ')