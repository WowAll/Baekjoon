n = int(input())

def num_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * num_hanoi(n - 1) + 1

def hanoi(cnt, start, temp, dest): 
    if cnt == 0:
        return
    hanoi(cnt - 1, start, dest, temp)
    print(start, dest)
    hanoi(cnt - 1, temp, start, dest)
print(num_hanoi(n))
if n <= 20:
    hanoi(n, 1, 2, 3)