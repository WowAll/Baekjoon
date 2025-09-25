import sys

def fibo(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibo(n - 1) + fibo(n - 2)
        return dp[n]

N = int(sys.stdin.readline().strip())

dp = [-1 for _ in range(100)]

dp[0] = 0
dp[1] = 1
dp[2] = 1

print(fibo(N))