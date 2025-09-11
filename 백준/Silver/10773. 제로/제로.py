import sys

t = int(sys.stdin.readline())

arr = []
sum = 0

for i in range(t):
    command = int(sys.stdin.readline())
    if command == 0:
        if arr:
            sum -= arr.pop()
    else:
        arr.append(command)
        sum += command
print(sum)