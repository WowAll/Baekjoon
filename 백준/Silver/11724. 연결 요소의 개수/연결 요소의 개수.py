import sys
from collections import deque

def find(arr, a):
    if arr[a] != a:
        arr[a] = find(arr,arr[a])
    return arr[a]

def union(arr, a, b):
    a_parent = find(arr, a)
    b_parent = find(arr, b)
    if a_parent == b_parent:
        return False
    if a_parent < b_parent:
        arr[b_parent] = a_parent
    else:
        arr[a_parent] = b_parent
    return True

N, M = map(int, sys.stdin.readline().strip().split())

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    union(parent, src, dest)
for i in range(1, N + 1):
    find(parent, i)
parent = parent[1:]
parent.sort()
print(len(set(parent)))