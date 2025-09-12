import sys

K, N = map(int, sys.stdin.readline().strip().split())

num = str(sys.stdin.readline().strip())

stack = []

cnt = 0

for i in num:
    if stack and stack[-1] < int(i) and cnt < N:
        while stack and stack[-1] < int(i) and cnt < N:
            stack.pop()
            cnt += 1
    stack.append(int(i))

while cnt < N:
    stack.pop()
    cnt += 1

for i in stack:
    print(i, end="")