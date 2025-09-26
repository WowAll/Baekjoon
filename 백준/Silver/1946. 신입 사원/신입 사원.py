import sys

tc = int(sys.stdin.readline().strip())
for i in range(tc):
    cnt = 0
    N = int(sys.stdin.readline().strip())
    scores = []
    for j in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        scores.append((a, b))
    
    scores.sort()
    b_top = 999999

    for _, b in scores:
        if b_top > b:
            cnt += 1
            b_top = b
    print(cnt)