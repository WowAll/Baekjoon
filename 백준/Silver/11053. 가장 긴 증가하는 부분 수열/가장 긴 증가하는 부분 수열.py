n = int(input())

arr = list(map(int, input().split()))

left = 0

right = n - 1

ans = 1

tails = []

def divide_search(arr, cur):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < cur:
            left = mid + 1
        else:
            right = mid - 1
    arr[left] = cur

tails.append(arr[0])
for i in range(1, n):
    if arr[i] > tails[-1]:
        tails.append(arr[i])
    else:
        divide_search(tails, arr[i])

print(len(tails))