import sys

sys.setrecursionlimit(10**5)

def input():
    INF = 2 ** 31 - 1
    M, N = map(int, sys.stdin.readline().split())

    arr = [[INF] * N for _ in range(M)]
    for i in range(M):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            arr[i][j] = temp[j]
    return (arr, M, N)

def func(arr, dp, scale, cur):
    M, N = scale
    x, y = cur
    if y == M - 1 and x == N - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] < arr[y][x]:
            dp[y][x] += func(arr, dp, (M, N), (nx, ny))
    return dp[y][x]


arr, M, N = input()
dp = [[-1] * N for _ in range(M)]
print(func(arr, dp, (M, N), (0, 0)))