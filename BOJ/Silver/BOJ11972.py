# https://www.acmicpc.net/problem/11972

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road = []
for i in range(N):
  l, spped = map(int, input().split())
  road += [spped for _ in range(l)]

run = []
for i in range(M):
  l, spped = map(int, input().split())
  run += [spped for _ in range(l)]

answer = 0
l = min(len(road), len(road))
for i in range(l):
  if run[i] > road[i]:
    answer = max(answer, run[i] - road[i])
print(answer)