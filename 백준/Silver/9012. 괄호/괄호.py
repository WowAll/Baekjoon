import sys

t = int(sys.stdin.readline())

for i in range(t):
    command = str(sys.stdin.readline())
    arr = []
    for j in command:
        if j == '(':
            arr.append(j)
        if j == ')':
            if not arr:
                arr.append(j)
                break
            else:
                arr.pop()
    if arr:
        print("NO")
    else:
        print("YES")