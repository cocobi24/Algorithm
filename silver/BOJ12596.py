# https://www.acmicpc.net/problem/12596

import sys
input = sys.stdin.readline

T = int(input())

for idx in range(1, T+1) :
  C = int(input())
  G = list(map(int, input().split()))
  sole = []
  for i in range(C) :
    if G[i] not in sole :
      sole.append(G[i])
    else :
      sole.remove(G[i])
  print(f"Case #{idx}: {sole[0]}")