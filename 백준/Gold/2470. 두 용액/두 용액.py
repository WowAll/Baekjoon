n = int(input())

arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

min_diff = 2000000000

while left < right:
    diff = arr[right] + arr[left]
    if abs(diff) < min_diff:
        min_diff = abs(diff)
        l_ans = left
        r_ans = right
    if diff > 0:
        right -= 1
    elif diff < 0:
        left += 1
    else:
        break
print(arr[l_ans], arr[r_ans])