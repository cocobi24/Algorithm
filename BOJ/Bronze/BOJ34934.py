# https://www.acmicpc.net/problem/34934

import sys
input = sys.stdin.readline

n = int(input())
ans = ''
for _ in range(n):
    s, y = input().rstrip().split()
    if y == '2026':
        ans = s
print(ans)