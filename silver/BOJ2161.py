# https://www.acmicpc.net/problem/2161

from collections import deque
n = int(input())
cards = deque([int(i) for i in range(1,n+1)])

while True :
    if len(cards) == 1 :
        print(*cards, end=" ")
        break
    discard = cards.popleft()
    tapcard = cards.popleft()
    cards.append(tapcard)
    print(discard, end=" ")