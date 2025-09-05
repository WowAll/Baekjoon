a, b = map(int, input().split())

fix_a = (a % 10) * 100 + ((a // 10) % 10) * 10 + a // 100
fix_b = (b % 10) * 100 + ((b // 10) % 10) * 10 + b // 100

if fix_a > fix_b:
    print(fix_a)
else:
    print(fix_b)