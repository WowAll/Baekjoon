import sys

s1 = str(sys.stdin.readline().strip())
s2 = str(sys.stdin.readline().strip())

ls1 = len(s1)
ls2 = len(s2)

dp = [[0] * (ls2 + 2) for _ in range(ls1 + 2)]

dp[0][0] = 0
for i in range(1, ls1 + 1):
    dp[i][0] = 0
for i in range(1, ls2 + 1):
    dp[0][i] = 0

for i in range(1, ls1 + 1):
    for j in range(1, ls2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[ls1][ls2])