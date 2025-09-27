import sys
from collections import deque

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(sys.stdin.readline())

arr = [[0] * N for i in range(N)]

fish = 0
cnt = 0
size = 2
eat = 0

for i in range(0, N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(0, N):
        arr[i][j] = row[j]
        if row[j] != 0 and row[j] != 9:
            fish += 1
        if row[j] == 9:
            shark_pos = [j, i]
            arr[i][j] = 0

def baby_shark(cur, size):
    global N, cnt
    cur_x, cur_y = cur
    q = deque()
    q.append([cur_x, cur_y, 0])

    fishes = []

    vis = [[False] * N for _ in range(N)]
    vis[cur_y][cur_x] = True
    while q:
        cur_x, cur_y, cur_cnt = q.popleft()
        if 0 < arr[cur_y][cur_x] < size:
            fishes.append((cur_cnt, cur_y, cur_x))
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N or vis[next_y][next_x] == True or arr[next_y][next_x] > size:
                continue
            vis[next_y][next_x] = True
            q.append([next_x, next_y, cur_cnt + 1])
    if not fishes:
        return [-1, -1]
    fishes.sort()
    cur_cnt, y, x = fishes[0]
    cnt += cur_cnt
    return [x, y]

while fish != 0:
    shark_pos = baby_shark(shark_pos, size)
    if shark_pos == [-1, -1]:
        break
    eat += 1
    arr[shark_pos[1]][shark_pos[0]] = 0
    if eat == size:
        size += 1
        eat = 0
    fish -= 1
print(cnt)