# https://www.acmicpc.net/problem/13617

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

goal = 0
for _ in range(N):
  info = list(map(int, input().split()))
  if 0 not in info:
    goal += 1
print(goal)