# https://www.acmicpc.net/problem/4158

import sys
input = sys.stdin.readline

while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  N_set = set(int(input()) for _ in range(N))
  M_set = set(int(input()) for _ in range(M))
  print(len(N_set & M_set))