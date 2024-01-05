# https://www.acmicpc.net/problem/9076

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  point = sorted(map(int, input().split()))[1:-1]
  total = sum(point)
  print('KIN' if max(point)-min(point) >=4 else total)