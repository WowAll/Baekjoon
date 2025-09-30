import sys

# sys.setrecursionlimit(10**6)

# def make_equation(i, j):
#     equation = []
#     for k in range(i, j + 1):
#         equation.append(str(num[k]))
#         if k != j:
#             equation.append(op[k])
#     return ''.join(equation)

# def backtracking(i, j):
#     if i == j:
#         return str(num[i])
#     else:
#         k = split[i][j]
#         if k == -1:
#             return '(' + make_equation(i, j) + ')'
#         left = backtracking(i, k)
#         right = backtracking(k + 1, j)
#         return str(left) + op[k] + str(right)

A = sys.stdin.readline().strip()

N = sys.stdin.readline().strip()

INF = 2**31 - 1

op = []

num = []

stack = []

temp = 0
for i in N:
    if i in '+-*':
        op.append(i)
        num.append(temp)
        temp = 0
    else:
        temp = temp * 10 + int(i)
    
num.append(temp)
length = len(num)

split = [[-1] * length for i in range(length)]

dp_max = [[-INF] * length for i in range(length)]
dp_min = [[INF] * length for i in range(length)]

for i in range(length):
    dp_max[i][i] = num[i]
    dp_min[i][i] = num[i]

for i in range(length - 1):
    if op[i] == '+':
        dp_max[i][i + 1] = num[i] + num[i + 1]
        dp_min[i][i + 1] = num[i] + num[i + 1]
    elif op[i] == '-':
        dp_max[i][i + 1] = num[i] - num[i + 1]
        dp_min[i][i + 1] = num[i] - num[i + 1]
    else:
        dp_max[i][i + 1] = num[i] * num[i + 1]
        dp_min[i][i + 1] = num[i] * num[i + 1]

for i in range(2, length):
    for j in range(0, length - i):
        k = j + i
        for l in range(j, k):
            temp_max = -INF
            temp_min = INF
            if op[l] == '+':
                temp_max = dp_max[j][l] + dp_max[l + 1][k]
                temp_min = dp_min[j][l] + dp_min[l + 1][k]
            elif op[l] == '-':
                temp_max = dp_max[j][l] - dp_min[l + 1][k]
                temp_min = dp_min[j][l] - dp_max[l + 1][k]
            else:
                temp_max = max(dp_max[j][l] * dp_max[l + 1][k], dp_max[j][l] * dp_min[l + 1][k], 
                            dp_min[j][l] * dp_max[l + 1][k], dp_min[j][l] * dp_min[l + 1][k])
                temp_min = min(dp_min[j][l] * dp_min[l + 1][k], dp_min[j][l] * dp_max[l + 1][k], 
                            dp_max[j][l] * dp_min[l + 1][k], dp_max[j][l] * dp_max[l + 1][k])  
            if temp_max > dp_max[j][k]:
                split[j][k] = l
                dp_max[j][k] = temp_max
            if temp_min < dp_min[j][k]:
                dp_min[j][k] = temp_min

print(dp_max[0][length - 1])

# print(backtracking(0, length - 1))