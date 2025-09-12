import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
arr = deque()
for i in range(N):
    arr.append(i + 1)

ans = 0
cnt = 1

ans = []

while arr:
    if cnt % M != 0:
        arr.append(arr.popleft())
    else:
        ans.append(arr.popleft())
    cnt += 1

print("<", end="")
for i in range(N):
    print(ans[i], end="")
    if i != N - 1:
        print(", ", end="")
print(">")