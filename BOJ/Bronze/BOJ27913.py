# https://www.acmicpc.net/problem/27913

import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

cnt = N // 10 * 3
mod = N % 10
if mod >= 7:
  cnt += 3
elif mod >= 4:
  cnt += 2
elif mod >= 1:
  cnt += 1

upper = {}

for _ in range(Q):
  X = int(input())
  if X in upper:
    if upper[X] == 0:
      upper[X] = 1
      cnt += 1
    else:
      upper[X] = 0
      cnt -= 1
  else:
    if X % 10 in [1, 4, 7]:
      upper[X] = 0
      cnt -= 1
    else:
      upper[X] = 1
      cnt += 1
  print(cnt)