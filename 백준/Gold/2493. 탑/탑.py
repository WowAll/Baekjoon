import sys

t = int(sys.stdin.readline())

arr = []
idx = []
ans = []
num = list(map(int, sys.stdin.readline().strip().split()))

for i in range(t):
    if not arr or arr[-1] > num[i]:
        if not arr:
            ans.append(0)
        else:
            ans.append(idx[-1] + 1)
        arr.append(num[i])
        idx.append(i)
    if arr[-1] < num[i]:
        while arr and arr[-1] <= num[i]:
            arr.pop()
            idx.pop()
        if arr:
            ans.append(idx[-1] + 1)
        else:
            ans.append(0)
        arr.append(num[i])
        idx.append(i)

for i in range(t):
    print(ans[i], end=' ')