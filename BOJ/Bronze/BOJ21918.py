# https://www.acmicpc.net/problem/21918

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
light_list = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        light_list[b-1] = c
    elif a == 2:
        for i in range(b - 1, c):
            light_list[i] = 1 if light_list[i] == 0 else 0
    else:
        light = 0 if a == 3 else 1
        for i in range(b - 1, c):
            light_list[i] = light

print(*light_list)