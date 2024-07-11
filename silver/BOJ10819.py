# https://www.acmicpc.net/problem/10819

from itertools import permutations
from collections import deque

n = int(input())
nums = sorted(map(int, input().rstrip().split()))
ans = 0
for p in permutations(nums):
  que = deque(p)
  l = que.pop()
  total = 0
  for i in range(1, n):
    if i % 2 == 0:
      l = que.pop()
    else:
      r = que.popleft()
    total += abs(l - r)
  if total > ans:
    ans = total
print(ans)