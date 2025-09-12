import sys
import heapq

N = int(sys.stdin.readline().strip())

arr = []
for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -num)