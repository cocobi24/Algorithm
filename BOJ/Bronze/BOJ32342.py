# https://www.acmicpc.net/problem/32342

import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
  cnt = 0
  s = input().rstrip()
  for i in range(0, len(s) - 2):
    if s[i:i+3] == "WOW":
      cnt += 1
  print(cnt)