# https://www.acmicpc.net/problem/31246

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
success = []
cnt = 0
for _ in range(N):
  a, b = map(int, input().split())
  if a >= b:
    cnt += 1
  else:
    success.append(b-a)
success.sort()

if cnt >= K:
  print(0)
else:
  x = 1
  for i in range(len(success)):
    if x - success[i] != 0:
      x += success[i] - x
      cnt += 1
    else:
      cnt += 1

    if cnt >= K:
      break

  print(x)