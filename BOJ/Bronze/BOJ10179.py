# https://www.acmicpc.net/problem/10179

import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  cost = float(input())
  sale = round(cost * 0.8, 2)
  print('${:0.2f}'.format(sale))