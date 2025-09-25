import sys
from collections import deque

INF = 2**31 - 1

tc = int(sys.stdin.readline().strip())

for i in range(tc):
    cnt = 0
    kinds = int(sys.stdin.readline().strip())
    coins = list(map(int ,sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())
    dp = [0  for _ in range(20000)]
    coins.sort()

    dp[0] = 1
   
    for coin in coins:
         for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    print(dp[target])