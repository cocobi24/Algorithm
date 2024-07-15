# https://www.acmicpc.net/problem/4458

import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    s = list(input().rstrip())
    s[0] = s[0].upper()
    print(''.join(s))