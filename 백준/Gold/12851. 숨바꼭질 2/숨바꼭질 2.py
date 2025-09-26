import sys
from collections import deque
INF = 2**31 - 1
N, K = map(int, sys.stdin.readline().strip().split())
q = deque()
count = 0
target = INF
vis = [INF] * 200001
cnt = [0] * 200001
flag = False
def move_pos(pos):
    arr = []
    if pos <= 99999:
        arr.append(pos + 1)
    if pos >= 1:
        arr.append(pos - 1)
    if pos <= 99999:
        arr.append(pos * 2)
    return arr
q.append((0, N))
cnt[N] = 1
vis[N] = 0
if N == K:
    print("0\n1")
    exit()
while q:
    cur_cnt, cur_pos = q.popleft()
    if cur_pos == K:
        print(cur_cnt)
        print(cnt[cur_pos])
        exit()
    for i in move_pos(cur_pos):
        if vis[i] == INF:
            q.append((cur_cnt + 1, i))
        if vis[i] >= cur_cnt:
            vis[i] = cur_cnt
            cnt[i] += cnt[cur_pos]

