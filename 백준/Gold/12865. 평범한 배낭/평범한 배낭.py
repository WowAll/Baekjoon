import sys

memo = {}

def knapsack(idx, w):
    global K, N
    next_idx = idx + 1
    if idx == N:
        return 0
    if (idx, w) in memo:
        return memo[(idx, w)]
    res = knapsack(next_idx, w)
    if w + weight[idx] <= K:
        res = max(res, knapsack(idx + 1, w + weight[idx]) + cost[idx])
    memo[(idx, w)] = res
    return res

N, K = map(int, sys.stdin.readline().strip().split())

weight = []
cost = []

for i in range(N):
    W, V = map(int, sys.stdin.readline().strip().split())
    weight.append(W)
    cost.append(V)
            
print(knapsack(0, 0))