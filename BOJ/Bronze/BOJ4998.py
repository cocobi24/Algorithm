# https://www.acmicpc.net/problem/4998

import sys
input = sys.stdin.readline
while True:
  i = input().rstrip()
  if len(i) == 0:
    break

  N, B, M = map(float, i.split())
  time = 0
  while M > N:
    time += 1
    N += N * (B/100)
  print(time)