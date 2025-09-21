import sys
sys.setrecursionlimit(10**6)

V = int(sys.stdin.readline().strip())

cnt = 0

def dfs(arr, vis, room, cur):
    global cnt
    if vis[cur]:
        return
    if room[cur] == 1:
        cnt += 2
        return
    vis[cur] = True
    for i in arr[cur]:
        dfs(arr, vis, room, i)
    vis[cur] = False

inout = str(sys.stdin.readline().strip())
room = []
room.append(0)
for i in inout:
    room.append(ord(i) - ord('0'))
arr = [[] for _ in range(V + 1)]

for i in range(V - 1):
    src, dest = map(int, sys.stdin.readline().strip().split())
    arr[src].append(dest)
    arr[dest].append(src)

vis = [False for _ in range(V + 1)]

for i in range(1, V + 1):
    if room[i] == 0:
        continue
    for J in arr[i]:
        vis[i] = True
        dfs(arr, vis, room, J)
print(cnt)