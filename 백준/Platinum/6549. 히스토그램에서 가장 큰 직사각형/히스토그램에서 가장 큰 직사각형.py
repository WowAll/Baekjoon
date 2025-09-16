import sys

def cal_scale(arr, left, right):
    mid = left + (right - left) // 2
    temp = arr[mid]
    res = temp
    left_cursor = mid - 1
    right_cursor = mid + 1
    len = 1
    unit = arr[mid]

    while res <= unit * (right - left + 1) :
        if left_cursor < left and right_cursor > right:
            return res
        if left_cursor >= left and right_cursor <= right:
            if arr[left_cursor] > arr[right_cursor]:
                selected = arr[left_cursor]
                left_cursor -= 1
            else:
                selected = arr[right_cursor]
                right_cursor += 1
        else:
            if left_cursor < left:
                selected = arr[right_cursor]
                right_cursor += 1
            else:
                selected = arr[left_cursor]
                left_cursor -= 1
        len += 1
        if selected > unit:
            temp += unit
        else:
            unit = selected
            temp = selected * len
        res = max(temp, res)
    return res

def histogram(arr, left, right):
    mid = left + (right - left) // 2
    if left >= right:
        return arr[mid]
    res = 0
    left_res = histogram(arr, left , mid - 1)
    right_res = histogram(arr, mid + 1, right)
    res = max(left_res, right_res)
    res = max(res, cal_scale(arr, left, right))
    return res

N = list(map(int, sys.stdin.readline().strip().split()))

while N[0] != 0:
    print(histogram(N[1:], 0, len(N[1:]) - 1))
    N = list(map(int, sys.stdin.readline().strip().split()))