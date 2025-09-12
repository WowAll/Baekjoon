import sys
from collections import deque

mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(K):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[y][x] = 1

L = int(sys.stdin.readline().strip())
request = {}
for i in range(L):
    time, dir = map(str, sys.stdin.readline().strip().split())
    request[time] = dir

snake = deque()
snake.append([1, 1])

cur_x = 1
cur_y = 1
cur_dir = 0
cnt = 0

while True:
    cnt += 1
    cur_x += mx[cur_dir]
    cur_y += my[cur_dir]
    if cur_x <= 0 or cur_y <= 0 or cur_x > N or cur_y > N:
        break
    if [cur_x, cur_y] in snake:
        break
    snake.append([cur_x, cur_y])
    if arr[cur_x][cur_y] == 1:
        arr[cur_x][cur_y] = 0
    else:
        snake.popleft()
    order = request.get(str(cnt))
    if order == 'L':
        cur_dir = (3 + cur_dir) % 4
    elif order == 'D':
        cur_dir = (1 + cur_dir) % 4

print(cnt)