import sys
import heapq

N = int(sys.stdin.readline().strip())

max_arr = []
min_arr = []
cnt = 0
for i in range(N):
    cnt += 1
    num = int(sys.stdin.readline().strip())
    heapq.heappush(max_arr, -num)
    if min_arr and -max_arr[0] > min_arr[0]:
        max_temp = heapq.heappop(max_arr)
        min_temp = heapq.heappop(min_arr)
        heapq.heappush(max_arr, -min_temp)
        heapq.heappush(min_arr, -max_temp)
    if len(max_arr) - len(min_arr) > 1:
        heapq.heappush(min_arr, -heapq.heappop(max_arr))
    print(-max_arr[0])
