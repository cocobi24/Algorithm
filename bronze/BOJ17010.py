# https://www.acmicpc.net/problem/17010

import sys
input = sys.stdin.readline
l = int(input())

for _ in range(l):
  n, x = map(str, input().split())
  print(int(n) * x)