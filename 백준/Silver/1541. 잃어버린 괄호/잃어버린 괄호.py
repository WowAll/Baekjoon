import sys

func = str(sys.stdin.readline().strip())

ans = 0
temp = 0
flag = False
for i in func:
    if i == '-' or i == '+':
        if flag:
            ans -= temp
        else:
            ans += temp
        if i == '-':
            flag = True
        temp = 0
    else:
        temp *= 10
        temp += ord(i) - ord('0')
if flag:
    ans -= temp
else:
    ans += temp

print(ans)