def merge_sort(arr):
    merge = []
    big = []
    small = []
    pivot = arr[0]
    for i in arr[1:]:
        if pivot > i:
            small.append(i)
        else:
            big.append(i)
    if len(big) > 1:
        big = merge_sort(big)
    if len(small) > 1:
        small = merge_sort(small)
    for i in small:
        merge.append(i)
    merge.append(pivot)
    for i in big:
        merge.append(i)
    return merge

n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
arr = merge_sort(arr)
for i in arr:
    print(i)