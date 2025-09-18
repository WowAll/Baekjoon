import sys

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

hashmap = dict()

for i in arr:
    hashmap[i] = 1

M = int(sys.stdin.readline().strip())

search = list(map(int, sys.stdin.readline().strip().split()))

for i in search:
    if hashmap.get(i):
        print(1, end=" ")
    else:
        print(0, end=" ")