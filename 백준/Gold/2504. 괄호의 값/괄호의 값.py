import sys

word = str(sys.stdin.readline())

cur = 0
sum = []
stack = []
ans = 0

for i in word:
    if i == '(' or i == '[':
        stack.append(i)
        sum.append(cur)
        cur = 0
    if i == ')':
        if not stack or stack[-1] != '(':
            stack.append(i)
            break
        if cur == 0:
            cur = 2
        else:
            cur *= 2
        if sum:
            cur += sum.pop()
        stack.pop()
    if i == ']':
        if not stack or stack[-1] != '[':
            stack.append(i)
            break
        if cur == 0:
            cur = 3
        else:
            cur *= 3
        if sum:
            cur += sum.pop()
        stack.pop()
    ans = cur

if stack:
    print(0)
else:
    print(ans)