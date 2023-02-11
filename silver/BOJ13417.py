# https://www.acmicpc.net/problem/13417

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n = int(input())
    chars = deque(input().replace(' ', '').rstrip())
    answer = deque(chars.popleft())

    for char in chars :
        prev = answer.popleft()
        answer.appendleft(prev)
        if ord(prev) >= ord(char) :
            answer.appendleft(char)
        else :
            answer.append(char)
    print(''.join(answer))
