import sys
sys.setrecursionlimit(10**6)

def dfs(arr, vis, cur):
    vis[cur] = True
    for i in arr[cur]:
        if not vis[i]:
            parent[i] = cur
            dfs(arr, vis, i)
            vis[i] = True

N = int(sys.stdin.readline().strip())

arr = [[] for _ in range(N + 1)]

parent = [0] * (N + 1)

for i in range(N - 1):
    src, dest = map(int, sys.stdin.readline().strip().split())
    arr[src].append(dest)
    arr[dest].append(src)
vis = [False] * (N + 1)

vis[1] = True
dfs(arr, vis, 1)
for i in parent[2:]:
    print(i)