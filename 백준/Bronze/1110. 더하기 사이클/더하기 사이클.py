def newnum(n, origin):
    if n == origin:
        return 1
    else:
        num = (n % 10) + (n // 10)
        return 1 + newnum(n % 10 * 10 + num % 10, origin)
    
num = int(input())
first = ((num % 10 + num // 10) % 10) + num % 10 * 10
print(newnum(first, num))