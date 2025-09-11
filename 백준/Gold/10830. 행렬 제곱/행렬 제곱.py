import sys

def modular(arr):
    for i in range(N):
        for j in range(N):
            arr[i][j] %= 1000
    return arr

def square_matrix(arr):
    return multiple_matrix(arr, arr)

def multiple_matrix(arr1, arr2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] %= 1000
    return result

def multiple(arr, n):
    if n == 1:
        return modular(arr)
    if n % 2 == 0:
        return square_matrix(multiple(arr, n // 2))
    else:
        return multiple_matrix(square_matrix(multiple(arr, n // 2)), arr)

arr = []
N, B = map(int, sys.stdin.readline().split())
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)
arr = multiple(arr, B)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
