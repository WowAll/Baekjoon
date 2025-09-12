import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []
ans = 0
for i in range(N):
    h, a = map(int, sys.stdin.readline().strip().split())
    if h > a:
        h, a = a, h
    heapq.heappush(arr, [a, h])
D = int(sys.stdin.readline().strip())
selected = []
while arr:
    cur = heapq.heappop(arr)
    if cur[0] - cur[1] > D:
        continue
    if not selected:
        cur[0], cur[1] = cur[1], cur[0]
        heapq.heappush(selected, cur)
    else:
        while selected and selected[0][0] + D < cur[0]:
            heapq.heappop(selected)
        cur[0], cur[1] = cur[1], cur[0]
        heapq.heappush(selected, cur)
    ans = max(ans, len(selected))
print(ans)