# https://www.acmicpc.net/problem/14670

import sys
input = sys.stdin.readline

N, M = int(input()), {}
for _ in range(N):
  e, n = map(int, input().split())
  M[e] = n

R = int(input())
for _ in range(R):
  L = list(map(int, input().split()))
  pill = []
  for i in range(1, len(L)):
    if L[i] in M:
      pill.append(M[L[i]])
    else:
      pill = "YOU DIED"
      break
  if pill != "YOU DIED":
    print(*pill)
  else:
    print(pill)