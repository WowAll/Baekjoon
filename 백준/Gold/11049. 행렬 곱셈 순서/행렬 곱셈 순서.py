import sys

INF = 2 ** 31 - 1

N = int(sys.stdin.readline().strip())

dp = [[0] * (N + 1) for _ in range(N+1)]

matrix = []

for i in range(N):
    r, c = map(int, sys.stdin.readline().strip().split())
    if i == 0:
        matrix.append(r)
    matrix.append(c)

for length in range(2, N + 1):
    for i in range(1, N - length + 2):
        j = i + length - 1
        dp[i][j] = INF
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix[i - 1] * matrix[j] * matrix[k])
print(dp[1][N])