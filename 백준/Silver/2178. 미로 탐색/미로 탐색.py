import sys
from collections import deque
sys.setrecursionlimit(10**6)

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

INF = 2 ** 32 - 1

N, M = map(int, sys.stdin.readline().strip().split())

arr = [[0] * M for _ in range(N)]

vis = [[False] * M for _ in range(N)]

for i in range(N):
    line = str(sys.stdin.readline().strip())
    for j in range(M):
        arr[i][j] = line[j]

q = deque()

q.append((1, 0, 0))
vis[0][0] = True

while q:
    cost, cur_x, cur_y = q.popleft()
    if cur_x == N - 1 and cur_y == M - 1:
        print(cost)
        exit()
    for i in range(4):
        nx = cur_x + mx[i]
        ny = cur_y + my[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if vis[nx][ny] == False and arr[nx][ny] == '1':
            vis[nx][ny] = True
            q.append((cost + 1, nx, ny))