n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
INF = 10**9

dp = [INF] * (k + 1)

arr = list(set(arr))

def dp_search():
    queue = [[0, 0]]
    while queue:
        now, cnt = queue.pop(0)
        if cnt >= dp[k]:
            break
        for i in arr:
            next = now + i
            if next > k:
                continue
            else:
                if dp[next] > cnt + 1:
                    dp[next] = cnt + 1
                    queue.append([next, cnt + 1])
dp_search()
if dp[k] == INF:
    print(-1)
else:  
    print(dp[k])