def backtracking(temp, idx, sum):
    global ans
    if idx >= N:
        if sum == S and temp:
            ans += 1
        return
    temp.append(arr[idx])
    backtracking(temp, idx + 1, sum + arr[idx])
    temp.pop()
    backtracking(temp, idx + 1, sum)

N, S = map(int, input().split())

arr = list(map(int, input().split()))

temp = []
ans = 0
backtracking(temp, 0, 0)
print(ans)