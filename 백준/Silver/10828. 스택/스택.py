import sys

t = int(sys.stdin.readline())

arr = []

for i in range(t):
    command= str(sys.stdin.readline().strip())
    if "push" in command:
        N = command.split()[1]
        arr.append(N)
    if command == "top":
        if arr:
            print(arr[-1])
        else:
            print(-1)
    if command == "size":
        print(len(arr))
    if command == "pop":
        if arr:
            print(arr.pop())
        else:
            print(-1)
    if command == "empty":
        if not arr:
            print(1)
        else:
            print(0)
