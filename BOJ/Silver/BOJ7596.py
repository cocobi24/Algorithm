# https://www.acmicpc.net/problem/7596

import sys
input = sys.stdin.readline

idx = 1
while True:
  T = int(input())
  if T == 0:
    break
  songs = sorted(input().rstrip() for _ in range(T))
  print(idx)
  print(*songs, sep='\n')
  idx += 1