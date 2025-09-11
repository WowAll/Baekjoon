def coin(n):
    ans = 0
    if n >= 3:
        ans += coin(n - 3)
    if n >= 2:
        ans += coin(n - 2)
    if n >= 1:
        ans += coin(n - 1)
    else:
        return 1
    return ans

num = int(input())
for i in range(num):
    print(coin(int(input())))