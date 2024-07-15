# https://www.acmicpc.net/problem/13975

import sys, heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  K = int(input())
  size = []
  total = 0
  for s in list(map(int, input().split())):
    heapq.heappush(size, s)
  while len(size) > 1:
    a = heapq.heappop(size)
    b = heapq.heappop(size)
    ab = a + b
    heapq.heappush(size, ab)
    total += ab
  print(total)