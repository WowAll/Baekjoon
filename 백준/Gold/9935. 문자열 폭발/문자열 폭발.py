import sys
from collections import deque

word = str(sys.stdin.readline().strip().split())
bomb = str(sys.stdin.readline().strip().split())
word = word[2:len(word) - 2]
bomb = bomb[2:len(bomb) - 2]

stack = []

idx = 0

while idx < len(word):
    stack.append(word[idx])
    if len(stack) >= len(bomb):
       cnt = 0
       while stack and (cnt == len(bomb) or stack[len(stack) - 1 - cnt] == bomb[len(bomb) - 1 - cnt]):
            if cnt == len(bomb):
                for i in range(len(bomb)):
                   stack.pop()
                cnt = 0
                continue
            cnt += 1
    idx += 1

if not stack:
    print("FRULA")
else:
    for i in stack:
        print(i, end="")