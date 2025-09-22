import sys
from collections import deque
sys.setrecursionlimit(10**6)

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

INF = 2 ** 32 - 1

N, M, K, X = map(int, sys.stdin.readline().strip().split())

arr = [[] for _ in range(N + 1)]
vis = [False] * (N + 1)

for i in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    arr[src].append(dest)
q = deque()

q.append((0, X))
vis[X] = True
ans = []

while q:
    cost, src = q.popleft()
    if cost > K:
        while q:
            q.pop()
    if cost == K:
        ans.append(src)
    for i in arr[src]:
        if not vis[i]:
            q.append((cost + 1, i))
            vis[i] = True

ans.sort()

if not ans:
    print(-1)
else:
    for i in ans:
        print(i)