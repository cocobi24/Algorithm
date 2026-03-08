# https://www.acmicpc.net/problem/6721

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x, y = input().split()
    x = int(x[::-1])
    y = int(y[::-1])
    xy = int(str(x + y)[::-1])
    print(xy)