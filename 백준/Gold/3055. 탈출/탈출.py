import sys
from collections import deque

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().strip().split())

arr = [[' '] * N for _ in range(M)]

q = deque()
water = deque()

vis = [[False] * N for _ in range(M)]

for i in range(M):
    col = str(sys.stdin.readline().strip())
    for j in range(N):
        arr[i][j] = col[j]
        if col[j] == '*':
            water.append((j, i))
        if col[j] == 'S':
            q.append((1, j, i))
            vis[i][j] = True
while q:
    for i in range(len(q)):
        cur_time, cur_x, cur_y = q.popleft()
        if arr[cur_y][cur_x] == '*':
            continue
        for i in range(4):
            nx = cur_x + mx[i]
            ny = cur_y + my[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or arr[ny][nx] == 'X' or arr[ny][nx] == '*' or vis[ny][nx] == True:
                continue
            if arr[ny][nx] == 'D':
                print(cur_time)
                exit()
            q.append((cur_time + 1, nx, ny))
            vis[ny][nx] = True
    for i in range(len(water)):
        cur_x, cur_y = water.popleft()
        for i in range(4):
            nx = cur_x + mx[i]
            ny = cur_y + my[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or arr[ny][nx] == 'X' or arr[ny][nx] == '*' or arr[ny][nx] == 'D':
                continue
            arr[ny][nx] = '*'
            water.append((nx, ny))
print("KAKTUS")