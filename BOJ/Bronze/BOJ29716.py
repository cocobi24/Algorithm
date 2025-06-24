# https://www.acmicpc.net/problem/29716

import sys
input = sys.stdin.readline

J, N = map(int, input().split())
answer = 0
for i in range(N):
    weeds = input().rstrip()
    size = 0
    for w in weeds:
        if w.isupper():
            size += 4
        elif w.islower() or w.isdigit():
            size += 2
        elif w == ' ':
            size += 1
    if J >= size:
        answer += 1
print(answer)