import sys

arr = [0] * 10001
n = int(input())
for i in range(n):
    arr[(int(sys.stdin.readline()))] += 1

cnt = 0
idx = 1
while not cnt == n:
    if not arr[idx] == 0:
        for i in range(arr[idx]):
            print(idx)
        cnt += arr[idx]
    idx += 1