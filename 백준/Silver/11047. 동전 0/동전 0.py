import sys

N, K = map(int, sys.stdin.readline().strip().split())
coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline().strip()))
coin = coins.pop()
cnt = 0
while K != 0:
    while K < coin:
        coin = coins.pop()
    cnt += K // coin
    K = K % coin
print(cnt)