import sys
sys.setrecursionlimit(10 ** 5)

def recursion(dp, coin, w, i):
    if w == 0:
        return 0
    if i >= 2 or w < 0:
        return 2 ** 31 - 1
    if dp[w][i] != -1:
        return dp[w][i]
    ret = min(recursion(dp, coin, w - coin[i], i) + 1 ,recursion(dp, coin, w, i + 1)) 
    dp[w][i] = ret
    return ret

N = int(sys.stdin.readline())

dp = [[-1] * 2 for _ in range(N + 1)]

ans = recursion(dp, [2, 5], N, 0)
if ans == 2 ** 31 - 1:
    print(-1)
else:
    print(ans)