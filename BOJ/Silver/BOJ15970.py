# https://www.acmicpc.net/problem/15970

import sys
input = sys.stdin.readline
n = int(input())

dot_list = [[] for _ in range(n)]
for _ in range(n):
    x, y = map(int,input().split())
    dot_list[y-1].append(x)

answer = 0
for dot in dot_list:
    l = len(dot)
    dot.sort()

    if l <= 1:
      continue

    answer += abs(dot[0] - dot[1]) + abs(dot[-1] - dot[-2])
    for i in range(1, l-1):
        answer += min(abs(dot[i] - dot[i-1]), abs(dot[i] - dot[i+1]))

print(answer)