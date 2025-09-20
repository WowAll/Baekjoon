import sys
sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline().strip())

def dfs(arr, vis, cur, now):
        global flag
        vis[cur] = now
        if not flag:
            return
        for i in arr[cur]:
            if vis[i] == now:
                flag = False
                return
            if vis[i] == 0:
                dfs(arr, vis, i, -now)


for i in range(K):
    flag = True
    V, E = map(int, sys.stdin.readline().strip().split())
    arr = [[] for _ in range(V + 1)]

    for i in range(E):
        src, dest = map(int, sys.stdin.readline().strip().split())
        arr[src].append(dest)
        arr[dest].append(src)
    vis = [0 for i in range(V + 1)]

    for i in range(1, V + 1):
        if flag == False:
            break
        if vis[i] == 0:
            dfs(arr, vis, i, 1)

    if flag:
        print("YES")
    else:
        print("NO")