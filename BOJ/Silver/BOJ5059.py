# https://www.acmicpc.net/problem/5059

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  n = int(input())
  cost = sorted(map(int, input().split()), reverse=True)
  total = 0
  for i in range(2, n, 3):
    total += cost[i]
  print(total)