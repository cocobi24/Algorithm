# https://www.acmicpc.net/problem/9935

import sys
from collections import deque

input = sys.stdin.readline
str = input().rstrip()

bomb = input().rstrip()
bomb_len = len(bomb)
last_bomb = bomb[-1]

queue = deque()

for s in str :
    queue.append(s)

    if (len(queue) >= bomb_len) and (s == last_bomb) :
        temp = ''
        for i in range(bomb_len) :
            ps = queue.pop()
            temp += ps
        if temp[::-1] != bomb :
            queue += temp[::-1]

if len(queue) >= 1 :
    print(''.join(queue), end='')
else :
    print("FRULA", end='')