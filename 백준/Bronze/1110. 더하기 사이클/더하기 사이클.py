def makenum(n):
    temp = n // 10 + n % 10
    return (n % 10) * 10 + temp % 10
def cycle(n, origin):
    newnum = makenum(n)
    if newnum == origin:
        return 1
    return 1 + cycle(newnum, origin)
num = int(input())
print(cycle(num, num))