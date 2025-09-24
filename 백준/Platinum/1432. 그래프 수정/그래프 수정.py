import sys
import heapq

N = int(sys.stdin.readline().strip())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
res = [0] * (N + 1)

pq = []
num = N

for i in range(N):
    word = str(sys.stdin.readline().strip())
    for j in range(N):
        if word[j] == '1':
            graph[j + 1].append(i + 1)
            indegree[i + 1] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, -i)
while pq:
    cur = -heapq.heappop(pq)
    res[cur] = num
    num -= 1
    for next in graph[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(pq, -next)

if num != 0:
    print(-1)
    exit()

for i in res[1:]:
    print(i, end=" ")

print()
