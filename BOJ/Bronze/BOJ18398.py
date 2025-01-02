# https://www.acmicpc.net/problem/18398

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        print(x+y, x*y)