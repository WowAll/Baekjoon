n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while(start <= end):
    cnt = 1
    cur = arr[0]
    mid = (start + end) // 2

    for i in range(1, n):
        if arr[i] >= cur + mid:
            cnt += 1
            cur = arr[i]
    
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)