import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [[' '] * M for _ in range(N)]
vis = [[False]* M for _ in range(N)]
cnt = 0

def dfs(cur_x, cur_y, type):
    if cur_x >= M or cur_y >= N or arr[cur_y][cur_x] != type:
        return
    vis[cur_y][cur_x] = True
    if type == '-':
        dfs(cur_x + 1, cur_y, type)
    else:
        dfs(cur_x, cur_y + 1, type)

for i in range(N):
    word = input().strip()
    for j in range(M):
        arr[i][j] = word[j]

for i in range(N):
    for j in range(M):
        if vis[i][j]:
            continue
        cnt += 1
        dfs(j, i, arr[i][j])

print(cnt)
    