import sys

N = int(sys.stdin.readline().strip())

meetings = []

for i in range(N):
    s, d = map(int, sys.stdin.readline().strip().split())
    meetings.append((d, s))

last = 0
cnt = 0

meetings.sort()

for dest, src in meetings:
    if src >= last:
        cnt += 1
        last = dest
    
print(cnt)