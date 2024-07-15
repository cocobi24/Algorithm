# https://www.acmicpc.net/problem/30022

import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())

stores = []
for _ in range(N):
  p, q = map(int, input().split())
  stores.append([p, q, p-q])
stores.sort(key=lambda x: -abs(x[2]))

l, r, total = 0, 0, 0
for i in range(N):
  if l == A:
    total += stores[i][1]
  elif r == B:
    total += stores[i][0]
  elif stores[i][2] > 0:
    total += stores[i][1]
    r += 1
  else:
    total += stores[i][0]
    l += 1
print(total)