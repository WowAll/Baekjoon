a, b, v = map(int, input().split())
ans = (v-a)//(a-b) + 1
if (v-a)%(a-b) != 0:
    ans += 1
print(ans)