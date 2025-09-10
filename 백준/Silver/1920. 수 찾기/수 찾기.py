n = int(input())

arr = list(map(int, input().split()))

cnt = {}

for i in arr:
    cnt[i] = True

n = int(input())

arr = list(map(int, input().split()))

for i in arr:
    if cnt.get(i):
        print(1)
    else:
        print(0)