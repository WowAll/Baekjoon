import sys
import heapq

sys.setrecursionlimit(10**6)

V, E = map(int, sys.stdin.readline().strip().split())

parent = [0] * (V + 1)

for i in range(V + 1):
    parent[i] = i

def find_parent(arr, a):
    cur = a
    if arr[a] != a:
        arr[a] = find_parent(arr, arr[a])
    return arr[a]

def union_parent(arr, a, b):
    a_parent = find_parent(arr, a)
    b_parent = find_parent(arr, b)
    if a_parent != b_parent:
        arr[b_parent] = a_parent
        return True
    return False

pq = []

res = 0
cnt = 0

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(pq, [c, [a, b]])

while cnt < V - 1 and pq:
    cost, edge = heapq.heappop(pq)
    if union_parent(parent, edge[0], edge[1]):
        res += cost
        cnt += 1
print(res)