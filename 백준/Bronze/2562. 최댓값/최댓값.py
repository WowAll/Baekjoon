a = []
for i in range(9):
    a.append(int(input()))

max = 0
idx = 0
for i in range(len(a)):
    if a[i] > max:
        idx = i
        max = a[i]
print(max)
print(idx + 1)