# https://www.acmicpc.net/problem/5555

import sys
from collections import deque
input = sys.stdin.readline
target = input().rstrip()
n = int(input())
answer = 0

for _ in range(n) :
    ring = input().rstrip()
    if target in ring :
        answer += 1
        continue

    ring = deque(ring)
    for i in range(len(ring)) :
        ring.rotate(-1)
        temp = ''.join(ring)
        if target in temp:
            answer += 1
            break

print(answer)