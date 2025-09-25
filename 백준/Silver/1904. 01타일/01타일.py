import sys

N = int(sys.stdin.readline().strip())

dp = [-1 for _ in range(N + 3)]

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])