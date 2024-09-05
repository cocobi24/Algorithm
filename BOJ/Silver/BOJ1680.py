# https://www.acmicpc.net/problem/1680

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  W, N = map(int, input().split())
  garbage = [list(map(int, input().split())) for i in range(N)]
  cart, distance = garbage[0][1], garbage[0][0]
  for i in range(1, N):
    if cart == W:
      distance += garbage[i-1][0] + garbage[i][0]
      cart = 0
    else:
      distance += garbage[i][0] - garbage[i-1][0]

    if cart + garbage[i][1] > W:
      distance += garbage[i][0] * 2
      cart = garbage[i][1]
    else:
      cart += garbage[i][1]

  distance += garbage[-1][0]
  print(distance)