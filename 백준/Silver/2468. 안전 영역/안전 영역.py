import sys
sys.setrecursionlimit(100000)

ans = 1

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

n = int(input())

def reset():
    global n
    for i in range(n):
        for j in range(n):
            vis[i][j] = False

def check_island(x, y, height):
    vis[x][y] = True
    for i in range(4):
        nx = mx[i] + x
        ny = my[i] + y
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue
        if arr[nx][ny] > height and not vis[nx][ny]:
            check_island(nx, ny, height)


arr = []
type = set()
for i in range(n):
    row = list(map(int, input().split()))
    for i in row:
        type.add(i)
    arr.append(row)
lst = list(type)
lst.sort()

vis = []
for i in range(n):
    vis.append([False] * n)

for i in lst:
    reset()
    cnt = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and not vis[j][k]:
                cnt += 1
                check_island(j, k, i)
    ans = max(ans, cnt)
print(ans)