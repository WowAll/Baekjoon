import sys

N, K = map(int, sys.stdin.readline().strip().split())
use = list(map(int, sys.stdin.readline().strip().split()))

times = {}
for i in range(K - 1, -1, -1):
    times[use[i]] = times.get(use[i], [])
    times[use[i]].append(i)
connected = {}
ans = 0
for i in use:
    times[i].pop()
    if connected.get(i):
        continue
    if len(connected) == N:
        idx = 0
        far = 0
        for key in connected:
            c = times.get(key)
            if c:
                if far < c[-1]:
                    idx = key
                    far = c[-1]
            else:
                idx = key
                far = K + 1
        del connected[idx]
        ans += 1
    connected[i] = 1
print(ans)