import sys
from collections import deque

word = str(sys.stdin.readline().strip().split())
bomb = str(sys.stdin.readline().strip().split())

# '[', ''', ']'를 지워주는거
word = word[2:len(word) - 2]
bomb = bomb[2:len(bomb) - 2]

# 초기화된 스택 선언
stack = []

idx = 0

# word의 길이만큼 수행한다
while idx < len(word):
    # stack에 idx 위치의 word를 append
    stack.append(word[idx])

    # stack과 bomb의 비교 회수
    cnt = 0
  
    # stack이 bomb보다 작을 경우 폭탄이 터지지 않고
    # 맨 뒤 요소부터 순차적으로 탐색
    while len(stack) >= len(bomb) and (cnt == len(bomb) or stack[len(stack) - 1 - cnt] == bomb[len(bomb) - 1 - cnt]):
        
        # 만약 bomb와 비교가 끝났다 = cnt가 bomb의 len과 같다
        if cnt == len(bomb):

            # len(bomb)만큼 pop해준다
            for i in range(len(bomb)):
                stack.pop()
            
            break
        cnt += 1
    idx += 1

if not stack:
    print("FRULA")
else:
    for i in stack:
        print(i, end="")