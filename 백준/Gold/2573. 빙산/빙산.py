import sys
from collections import deque
sys.setrecursionlimit(10**6)

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

def find_iceberg():
    global M, N
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                return i, j

def bfs():
    global N, M, melted
    cnt = 0
    q = deque()
    x, y = find_iceberg()
    q.append((x, y))
    vis = [[False] * M for _ in range(N)]
    vis[x][y] = True
    while q:
        cnt += 1
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + mx[i]
            ny = cur_y + my[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if not vis[nx][ny] and arr[nx][ny] > 0:
                q.append((nx, ny))
                vis[nx][ny] = True
            if vis[nx][ny] == False and arr[nx][ny] == 0 and arr[cur_x][cur_y] > 0:
                arr[cur_x][cur_y] -= 1
        if arr[cur_x][cur_y] == 0:
            melted += 1
    return cnt

N, M = list(map(int, sys.stdin.readline().strip().split()))
arr = []

iceberg = 0

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in arr[i]:
        if j != 0:
            iceberg += 1
cycle = 0
while iceberg != 0:
    melted = 0
    melting = bfs()
    if melting != iceberg:
        print(cycle)
        exit()
    iceberg -= melted
    cycle += 1

print(0)