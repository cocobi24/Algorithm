# https://www.acmicpc.net/problem/3486

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = input().rstrip().split()
    x = int(num[0][::-1])
    y = int(num[1][::-1])
    answer = str(x + y)[::-1]
    print(int(answer))