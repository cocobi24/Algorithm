# https://www.acmicpc.net/problem/1302

import sys
input = sys.stdin.readline
n = int(input())
answer = {}

for i in range(n) :
    s = input().rstrip()
    if s in answer :
        answer[s] += 1
    else :
        answer[s] = 1

answer = sorted(answer.items(), key = lambda x : (-x[1], x[0]))
print(answer[0][0], end='')