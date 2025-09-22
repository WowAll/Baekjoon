import sys
sys.setrecursionlimit(10**6)

V = int(sys.stdin.readline().strip())

ans = 0

def dfs(cur):
    vis[cur] = True
    cnt = 0
    for i in arr[cur]:
        if room[i] == 1:
            cnt += 1
        elif not vis[i] and room[i] == 0:
            cnt += dfs(i)
    return cnt

inout = str(sys.stdin.readline().strip())
room = []
room.append(0)

vis = [False for _ in range(V + 1)]

for i in range(0, V):
    temp = ord(inout[i]) - ord('0')
    room.append(temp)

arr = [[] for _ in range(V + 1)]
connect = [0 for _ in range(V + 1)]

for i in range(V - 1):
    src, dest = map(int, sys.stdin.readline().strip().split())
    if room[src] == room[dest] and room[src] == 1:
        ans += 2
    else:
        arr[src].append(dest)
        arr[dest].append(src)

for i in range(1, V + 1): 
    if vis[i] == True:
        continue
    if room[i] == 0:
        temp = dfs(i)
        ans += (temp) * (temp - 1)
print(ans)