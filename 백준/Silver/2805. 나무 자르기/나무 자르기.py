n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = 0

right = max(arr)

ans = 0

while left <= right:
    tree = 0
    mid = (left + right) // 2

    for i in arr:
        if mid < i:
            tree += i - mid

    if m > tree:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)