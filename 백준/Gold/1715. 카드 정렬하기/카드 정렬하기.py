import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []
sum = 0
for i in range(N):
    num = int(sys.stdin.readline().strip())
    heapq.heappush(arr, num)
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum += (a + b)
    heapq.heappush(arr, a + b)
print(sum)