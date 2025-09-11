import sys

m_row = [0, 1, 0, 1]
m_col = [0, 0, 1, 1]

def is_color(n, row, col):
    global cnt

    cur = arr[row][col]
    if n == 0:
        return cur
    res = []
    for i in range(4):
        next_row = row + (2 ** (n - 1)) * m_row[i]
        next_col = col + (2 ** (n - 1)) * m_col[i]
        res.append(is_color(n - 1, next_row, next_col))
    if res[0] == res[1] == res[2] == res[3] != -1:
        if n == num:
            cnt[cur] += 1
        return res[0]
    else:
        for i in res:
            if i != -1:
                cnt[i] += 1
        return -1

cnt = [0, 0]

N = int(sys.stdin.readline())

arr = []

num = 1
while 2 ** num != N:
    num += 1

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

is_color(num, 0, 0)

print(cnt[0])
print(cnt[1])