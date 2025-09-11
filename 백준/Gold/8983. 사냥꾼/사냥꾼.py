import sys

def binary_search(tar):
    left = 0
    right = M - 1
    while left <= right:
        mid = (left + right) // 2
        if shooting[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1
    return left

def can_shoot(n, animal_x, animal_y):
    range = abs(shooting[n] - animal_x) + animal_y
    return range <= L

M, N, L = map(int, sys.stdin.readline().strip().split())

shooting = list(map(int, sys.stdin.readline().strip().split()))

shooting.sort()

ans = 0

for i in range(N):
    animal_x, animal_y = map(int, sys.stdin.readline().strip().split())
    if animal_y > L:
        continue
    idx = binary_search(animal_x)
    if idx < M and can_shoot(idx, animal_x, animal_y):
        ans += 1
        continue
    if idx > 0 and can_shoot(idx - 1, animal_x, animal_y):
        ans += 1

print(ans)