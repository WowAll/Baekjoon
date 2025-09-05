w, h = map(int, input().split())

n = int(input())

x = []
y = []
for i in range(n):
    command, line = map(int, input().split())
    if command == 0:
        y.append(line)
    else:
        x.append(line)
x.append(w)
y.append(h)
x.sort()
y.sort()
cur_x = 0
ans = 0
for i in x:
    cur_y = 0
    x_diff = i - cur_x
    for j in y:
        y_diff = j - cur_y
        ans = max(ans, x_diff * y_diff)
        cur_y = j
    cur_x = i
print(ans)