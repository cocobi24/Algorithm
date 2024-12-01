# https://www.acmicpc.net/problem/11098

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  C, name = 0, ""
  for i in range(n):
    c, n = input().rstrip().split()
    c = int(c)
    if c > C:
      C = c
      name = n
  print(name)