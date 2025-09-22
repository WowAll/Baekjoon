import sys
sys.setrecursionlimit(10**6)

def dfs_max(op, recur, res):
    global V
    ret = -(2**31 -1)
    if recur + 1 == V:
        return res
    for i in range(4):
        next = res
        if op[i] == 0:
            continue
        op[i] -= 1
        if i == 0:
            next += arr[recur + 1]
        elif i == 1:
            next -= arr[recur + 1]
        elif i == 2:
            next *= arr[recur + 1]
        else:
            if next < 0:
                next = -(-next // arr[recur + 1])
            else:
                next //= arr[recur + 1]
        ret = max(ret, dfs_max(op, recur + 1, next))
        op[i] += 1
    return ret

def dfs_min(op, recur, res):
    global V
    ret = 2**31 -1
    if recur + 1 == V:
        return res
    for i in range(4):
        next = res
        if op[i] == 0:
            continue
        op[i] -= 1
        if i == 0:
            next += arr[recur + 1]
        elif i == 1:
            next -= arr[recur + 1]
        elif i == 2:
            next *= arr[recur + 1]
        else:
            if next < 0:
                next = -(-next // arr[recur + 1])
            else:
                next //= arr[recur + 1]
        ret = min(ret, dfs_min(op, recur + 1, next))
        op[i] += 1
    return ret

V = int(sys.stdin.readline().strip())
arr = []

arr += list(map(int, sys.stdin.readline().strip().split()))

op = list(map(int, sys.stdin.readline().strip().split()))

print(dfs_max(op, 0, arr[0]))
print(dfs_min(op, 0, arr[0]))
        