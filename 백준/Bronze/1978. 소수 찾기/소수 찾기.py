is_prime = [True] * 1001
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(1001**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1001, i):
            is_prime[j] = False

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if is_prime[i]:
        cnt += 1
print(cnt)