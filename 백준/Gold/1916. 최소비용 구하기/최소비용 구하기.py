import sys
import heapq

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

INF = 2 ** 31 - 1

N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())

arr = [[] for _ in range(N + 1)]

dijkstra = [INF for _ in range(N + 1)]

pq = []

for i in range(M):
    src, dest, cost = map(int, sys.stdin.readline().strip().split())
    arr[src].append((cost, dest))

ans_s, ans_d = map(int, sys.stdin.readline().strip().split())

dijkstra[ans_s] = 0
heapq.heappush(pq, (0, ans_s))

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if(cur_cost > dijkstra[ans_d]):
        while pq:
            pq.pop()
    if cur_cost > dijkstra[cur_node]:
        continue
    for edge_cost, next_node in arr[cur_node]:
        next_cost = cur_cost + edge_cost
        if next_cost < dijkstra[next_node]:
            dijkstra[next_node] = next_cost
            heapq.heappush(pq, (next_cost, next_node))
print(dijkstra[ans_d])