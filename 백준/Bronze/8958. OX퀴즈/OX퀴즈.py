n = int(input())
for i in range(n):
    res = input()

    score = 0
    combo = 1
    for i in range(len(res)):
        if res[i] == "O":
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)