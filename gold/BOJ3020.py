# https://www.acmicpc.net/problem/3020

import sys
input = sys.stdin.readline
N, H = map(int, input().split())
obstacle = [0] * H

for i in range(N):
  block = int(input())
  if i % 2 == 0:
    obstacle[H-block] += 1
  elif i % 2 != 0:
    obstacle[block] -= 1
    obstacle[0] += 1

for i in range(1, H):
  obstacle[i] += obstacle[i-1]

min_obs = min(obstacle)
cnt = obstacle.count(min_obs)
print(min_obs, cnt)