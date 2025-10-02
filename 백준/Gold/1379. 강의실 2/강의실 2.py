import sys
from collections import deque
import heapq

N = int(sys.stdin.readline())

q = deque()

ans = [0] * N

for i in range(N):
    idx, start, end = map(int, sys.stdin.readline().split())
    q.append((start, end, idx))

q = deque(sorted(list(q)))

room_heap = []

room_count = 0

while q:
    start, end, idx = q.popleft()

    if room_heap and room_heap[0][0] <= start:
        finish, room_num = heapq.heappop(room_heap)
    else:
        room_count += 1
        room_num = room_count
    heapq.heappush(room_heap, (end, room_num))

    ans[idx - 1] = room_num

print(room_count)
for i in ans:
    print(i)