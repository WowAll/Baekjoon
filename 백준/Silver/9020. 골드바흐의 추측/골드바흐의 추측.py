is_prime = [True] * 10001
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(10001**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 10001, i):
            is_prime[j] = False

n = int(input())

for i in range(n):
    num = int(input())
    cur = num // 2
    while True:
        if is_prime[cur] and is_prime[num - cur]:
            print(cur, num - cur)
            break
        cur -= 1
