import sys

N = int(sys.stdin.readline().strip())

INF = (1 << 31) - 1

arr = []

def cal_distance(v1, v2):
    return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2

def find_spot(arr, left, right):
    if left >= right:
        return INF
    if left == right + 1:
        return cal_distance(arr[left], arr[right])
    mid = left + (right - left) // 2
    lres = find_spot(arr, left, mid - 1)
    rres = find_spot(arr, mid + 1, right)
    res = min(lres, rres)
    strip = arr[mid][0]
    temp = []
    for i in range(left, right):
        if (strip - arr[i][0]) ** 2 < res:
            temp.append(arr[i])
    
    temp.sort(key=lambda p:p[1])

    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if (temp[j][1] - temp[i][1]) ** 2 >= res:
                break
            res = min(res, cal_distance(temp[i], temp[j]))
    
    return res
    

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
arr.sort()

print(find_spot(arr, 0, N))