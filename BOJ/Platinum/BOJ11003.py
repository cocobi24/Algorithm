# https://www.acmicpc.net/problem/11003

import sys, heapq
input = sys.stdin.readline
n, l = tuple(map(int, input().split()))
a = list(map(int, input().split()))

d, temp = [], []
for i in range(n):
  heapq.heappush(temp, (a[i], i))

  while temp[0][1] < i - l + 1:
    heapq.heappop(temp)
  d.append(temp[0][0])

print(*d)