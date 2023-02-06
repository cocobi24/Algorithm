# https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline
n = int(input())
ranks = sorted([int(input()) for _ in range(n)])
answer = 0

for i in range(1, n+1):
    answer += abs(i-ranks[i-1])
print(answer)