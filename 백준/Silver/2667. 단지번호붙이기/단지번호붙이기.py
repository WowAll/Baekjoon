import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input().strip())
arr = [[' '] * N for _ in range(N)]
vis = [[False]* N for _ in range(N)]
cnt = 0
ans = []

def dfs(cur_x, cur_y):
    if cur_x >= N or cur_y >= N or cur_x < 0 or cur_y < 0 or vis[cur_y][cur_x] or arr[cur_y][cur_x] == '0':
        return 0
    vis[cur_y][cur_x] = True
    ret = 1
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        ret += dfs(next_x, next_y)
    return ret

for i in range(N):
    word = input().strip()
    for j in range(N):
        arr[i][j] = word[j]

for i in range(N):
    for j in range(N):
        if vis[i][j] or arr[i][j] == '0':
            continue
        cnt += 1
        ans.append(dfs(j, i))

ans.sort()

print(cnt)
for i in ans:
    print(i) 