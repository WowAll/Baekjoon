import sys
from collections import deque

mx = [-1, 1, 0, 0, 0, 0]
my = [0, 0, -1, 1, 0, 0]
mz = [0, 0, 0, 0, -1, 1]

INF = 2 ** 31 - 1

cnt = 0

M, N, H = map(int, sys.stdin.readline().strip().split())

arr = [[[' '] * M for _ in range(N)] for __ in range(H)]
vis = [[[False] * M for _ in range(N)] for __ in range(H)]
q = deque()
for k in range(H):
    for i in range(N):
        col = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(M):
            arr[k][i][j] = col[j]
            if col[j] != -1:
                cnt += 1
            if col[j] == 1:
                q.append((1, j, i, k))
                vis[k][i][j] = True
while q:
    cur_cost, cur_x, cur_y, cur_z = q.popleft()
    cnt -= 1
    if cnt == 0:
        print(cur_cost - 1)
        exit()
    for i in range(6):
        nx = cur_x + mx[i]
        ny = cur_y + my[i]
        nz = cur_z + mz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H or arr[nz][ny][nx] == -1 or vis[nz][ny][nx]:
            continue
        vis[nz][ny][nx] = True
        q.append((cur_cost + 1, nx, ny, nz))
print(-1)