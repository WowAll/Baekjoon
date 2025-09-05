n = int(input())

for i in range(n):
    avg = 0
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        avg += arr[j]
    avg = avg / arr[0]
    cnt = 0
    for j in range(1, arr[0] + 1):
        if arr[j] > avg:
            cnt += 1
    print("{:.3f}".format((cnt / arr[0]) * 100), "%")