import sys
import heapq
sys.setrecursionlimit(10**6)

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

INF = 2 ** 31 - 1

N = int(sys.stdin.readline().strip())

arr = [[' ']* N for _ in range(N)]
vis = [[False] * N for _ in range(N)]
pq = []
for i in range(N):
    col = str(sys.stdin.readline().strip())
    for j in range(N):
        arr[i][j] = col[j]

heapq.heappush(pq, (0, 0, 0))

while pq:
    cur_broken, cur_x, cur_y = heapq.heappop(pq)
    if cur_x == N - 1 and cur_y == N - 1:
        print(cur_broken)
        exit()
    if vis[cur_x][cur_y] == True:
        continue
    vis[cur_x][cur_y] = True
    if arr[cur_x][cur_y] == '0':
        next_broken = cur_broken + 1
    else:
        next_broken = cur_broken
    
    for i in range(4):
        nx = cur_x + mx[i]
        ny = cur_y + my[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        heapq.heappush(pq, (next_broken, nx, ny))
