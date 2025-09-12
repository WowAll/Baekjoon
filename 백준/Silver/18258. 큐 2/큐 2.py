import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = deque()
for i in range(N):
    command = str(sys.stdin.readline().strip())
    if command.find(" ") != -1:
        _, num = map(str, command.split())
        arr.append(num)
    elif command == "size":
        print(len(arr))
    elif command == "empty":
        if not arr:
            print(1)
        else:
            print(0)
    elif command == "pop":
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
    elif command == "front":
        if not arr:
            print(-1)
        else:
            print(arr[0])
    elif command == "back":
        if not arr:
            print(-1)
        else:
            print(arr[-1])