# https://www.acmicpc.net/problem/30970

import sys
input = sys.stdin.readline
n = int(input())
mini = [list(map(int, input().split())) for _ in range(n)]

mini.sort(key=lambda x:(-x[0], x[1]))
print(*mini[0], *mini[1])

mini.sort(key=lambda x:(x[1], -x[0]))
print(*mini[0], *mini[1])