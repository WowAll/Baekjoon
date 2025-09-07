import sys

def TSP(start, cur, cost):
    global ans
    if cost > ans:
        return
    if all(vis) and arr[cur][start]:
        ans = min(cost + arr[cur][start], ans)
    for i in range(n):
        if not arr[cur][i] == 0 and not vis[i]:
            vis[i] = True
            TSP(start, i, cost + arr[cur][i])
            vis[i] = False

n = int(input())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

vis = [False] * n

ans = 99999999

for i in range(n):
    vis[i] = True
    TSP(i, i, 0)
    vis[i] = False

print(ans)