import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = deque()
for i in range(N):
    arr.append(i + 1)

ans = 0

while len(arr) > 1:
    ans = arr.popleft()
    arr.append(arr.popleft())

print(arr[0])