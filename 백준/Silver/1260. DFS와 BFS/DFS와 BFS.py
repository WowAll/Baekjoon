import sys
from collections import deque

def dfs(arr, cur, vis):
    print(cur, end=" ")
    for i in arr[cur]:
        if not vis[i]:
            vis[i] = True
            dfs(arr, i, vis)
    return

def bfs(arr, root):
    print(root, end=" ")
    vis = [False] * (len(arr) + 1)
    vis[root] = True
    q = deque()
    for i in arr[root]:
        q.append(i)
        vis[i] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in arr[cur]:
            if not vis[i]:
                q.append(i)
                vis[i] = True

N, M, V = map(int, sys.stdin.readline().strip().split())

arr = [[] for _ in range(N + 1)]

vis = [False] * (N + 1)

for i in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    arr[src].append(dest)
    arr[dest].append(src)

for i in range(1, N+1):
    arr[i].sort()

vis[V] = True
dfs(arr, V, vis)
print()
bfs(arr, V)