# https://www.acmicpc.net/problem/14235

import sys, heapq
input = sys.stdin.readline

n = int(input())
present = []
for _ in range(n):
  a = input().rstrip()
  if len(a) == 1:
    print(heapq.heappop(present)[1] if len(present) > 0 else -1)
  else:
    for a in list(map(int, a.split()))[1:]:
      heapq.heappush(present, (-a, a))