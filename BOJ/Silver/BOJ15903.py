# https://www.acmicpc.net/problem/15903

import sys
from heapq import *
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
heapify(nums)

for _ in range(m):
  v = heappop(nums) + heappop(nums)
  heappush(nums, v)
  heappush(nums, v)
print(sum(nums))