def is_AP(num):
    a = num % 10
    b = (num // 10) % 10
    c = num // 100
    if a - b == b - c:
        return True

num = int(input())

arr = []
for i in range(100):
    arr.append(i)
if num >= 100:
    for i in range(100, num + 1):
        if is_AP(i):
            arr.append(arr[i-1] + 1)
        else:
            arr.append(arr[i-1])
print(arr[num])