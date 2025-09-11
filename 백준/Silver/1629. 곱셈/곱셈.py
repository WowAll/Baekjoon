import sys

def multiple(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (multiple(a, b // 2, c) ** 2) % c
    else:
        return ((multiple(a, b // 2, c) ** 2) * a) % c

A, B, C = map(int, sys.stdin.readline().split())

arr = []

print(multiple(A, B, C))