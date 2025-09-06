import sys

def heapify(arr, n, i):
    parent = i

    lc = 2 * i + 1
    rc = lc + 1

    if lc < n and arr[lc] > arr[parent]:
        parent = lc
    if rc < n and arr[rc] > arr[parent]:
        parent = rc
    
    if not parent == i:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr, n, parent)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = []
n = int(input())
for i in range(n):
    arr.append(int(sys.stdin.readline()))
heapsort(arr)
for i in arr:
    print(i)