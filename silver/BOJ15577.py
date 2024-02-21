# https://www.acmicpc.net/problem/15577

import sys, heapq
input = sys.stdin.readline
N = int(input())

nums = []
for _ in range(N):
  heapq.heappush(nums, int(input()))

for _ in range(N-1):
  a = heapq.heappop(nums)
  b = heapq.heappop(nums)
  c = (a+b)/2
  heapq.heappush(nums, c)
print(nums[0])