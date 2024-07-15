# https://www.acmicpc.net/problem/2170

import sys
input = sys.stdin.readline

N = int(input())
dot_list = sorted(tuple(map(int, input().split())) for _ in range(N))

start, end, answer = dot_list[0][0], dot_list[0][1], 0
for x, y in dot_list[1:]:
    if x > end:
        answer += (end - start)
        start = x
    end = max(end, y)
answer += (end - start)

print(answer)
