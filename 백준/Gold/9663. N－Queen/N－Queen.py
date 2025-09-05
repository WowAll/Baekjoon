ans = 0

def nqueen(col, ld, rd):
    if check == col:
        global ans
        ans += 1
        return
    valid_pos = check & ~(col | ld | rd)

    while valid_pos != 0:
        pos = valid_pos & -valid_pos
        valid_pos -= pos
        nqueen(col | pos, (ld | pos) << 1 , (rd | pos) >> 1)

n = int(input())
check = (1 << n) - 1

half = n // 2

for i in range(half):
    pos = 1 << i
    nqueen(pos, pos << 1, pos >> 1)
ans *= 2
if not n % 2 == 0:
    pos = 1 << half
    nqueen(pos, pos << 1 , pos >> 1)

print(ans)