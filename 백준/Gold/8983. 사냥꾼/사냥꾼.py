def binary_search(tar):
    left = 0
    right = M - 1
    shooter = left
    while left <= right:
        mid = (left + right) // 2
        if shooting[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1
            shooter = mid
    return shooter

def can_shoot(n, animal_x, animal_y):
    range = abs(shooting[n] - animal_x) + animal_y
    return range <= L

M, N, L = map(int, input().split())

shooting = list(map(int, input().split()))

shooting.sort()

ans = 0

for i in range(N):
    animal_x, animal_y = map(int, input().split())
    if can_shoot(binary_search(animal_x), animal_x, animal_y):
        ans += 1
print(ans)