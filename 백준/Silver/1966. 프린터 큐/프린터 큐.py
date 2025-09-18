import sys
from collections import deque

tc = int(sys.stdin.readline().strip())

for i in range(tc):
    cnt = 1
    job = deque()
    M, N = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for i in arr:
        job.append(i)
    while job:
        cur = job.popleft()
        if not job or cur >= max(job):
            if N == 0:
                break
            cnt += 1
            
        else:
            job.append(cur)
        N = (len(job) - 1 + N) % len(job)
    print(cnt)