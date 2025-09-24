import sys
import heapq
from collections import deque

INF = 2 ** 31 - 1

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)
indegree = [0] * (N + 1)
cnt = 0
vis = [False] * (N + 1)

q = deque()

for i in range(M):
    src, dest, cost = map(int, sys.stdin.readline().strip().split())
    graph1[src].append((cost, dest))
    graph2[dest].append((cost, src))
    indegree[dest] += 1

src, dest = map(int, sys.stdin.readline().strip().split())

q.append(src)
while q:
    cur = q.popleft()
    cur_time = dp[cur]
    for next_time, next in graph1[cur]:
        total = cur_time + next_time
        dp[next] = max(dp[next], dp[cur] + next_time)
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

q.append(dest)
while q:
    cur = q.popleft()
    for next_cost, next in graph2[cur]:
        if dp[cur] == next_cost + dp[next]:
            cnt += 1
            if not vis[next]:
                vis[next] = True
                q.append(next)
        
            

print(dp[dest])
print(cnt)