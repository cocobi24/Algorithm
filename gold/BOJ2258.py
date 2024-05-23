# https://www.acmicpc.net/problem/2258

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([list(map(int, input().split()))[::-1] for _ in range(n)], key = lambda x : (x[0], -x[1]))
ans, flag = 2147483648, False
weight, temp = 0, 0

for i in range(n):
  weight += nums[i][1]
  temp = temp + nums[i][0]if i >= 1 and nums[i][0] == nums[i - 1][0] else 0

  if weight >= m:
    ans = min(ans, nums[i][0] + temp)
    flag = True

print(ans if flag else -1)