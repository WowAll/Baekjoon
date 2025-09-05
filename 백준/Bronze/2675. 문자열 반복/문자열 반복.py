t = int(input())
for i in range(t):
    n, str = input().split()
    num = ord(n) - ord('0')
    for j in str:
        for k in range(num):
            print(j, end="")
    print()