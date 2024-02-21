# https://www.acmicpc.net/problem/29160

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
player = [[(0,0)] for _ in range(11)]
total = 0
for _ in range(N):
  P, W = map(int, input().split())
  heapq.heappush(player[P-1], (-W, W))

for _ in range(K):
  for i in range(11):
    best = heapq.heappop(player[i])
    if best[1]-1 < 0:
      heapq.heappush(player[i], (0, 0))
    else:
      heapq.heappush(player[i], (best[0]+1, best[1]-1))

total = 0
for i in range(11):
  best = heapq.heappop(player[i])
  total += best[1]
print(total)
