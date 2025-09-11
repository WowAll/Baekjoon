import sys

t = int(sys.stdin.readline())

arr = []
for i in range(t):
    num = int(sys.stdin.readline())
    if not arr or arr[-1] > num:
        arr.append(num)
    if arr[-1] < num:
        while arr and arr[-1] <= num:
            arr.pop()
        arr.append(num)
print(len(arr))