# https://www.acmicpc.net/problem/11008

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  s, copy = map(str, input().rstrip().split())
  print(len(s) - s.count(copy) * len(copy) + s.count(copy))