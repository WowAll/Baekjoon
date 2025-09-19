import sys

def dfs(arr, vis, cur):
    vis[cur] = True
    ret = 1
    for i in arr[cur]:
        if not vis[i]:
            ret += dfs(arr, vis, i)
            vis[i] = True
    return ret

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

arr = [[] for _ in range(N + 1)]

for i in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    arr[src].append(dest)
    arr[dest].append(src)
vis = [False] * (N + 1)

vis[1] = True
print(dfs(arr, vis, 1) - 1)