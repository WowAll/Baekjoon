import sys

def sum_diff(arr):
    sum = 0
    for i in range(len(arr) - 1):
        sum += abs(arr[i] - arr[i + 1])
    return sum

def diff_max(arr, vis, order, cnt):
    ans = 0
    if cnt == len(arr):
        return sum_diff(order)
    for i in range(len(arr)):
        if not vis[i]:
            vis[i] = True
            order.append(arr[i])
            ans = max(ans, diff_max(arr, vis, order, cnt + 1))
            order.pop()
            vis[i] = False
        
    return ans

n = int(input())

arr = list(map(int, input().split()))

vis = [False] * len(arr)
order = []

print(diff_max(arr, vis, order, 0))