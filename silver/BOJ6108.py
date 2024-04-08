# https://www.acmicpc.net/problem/6108

import sys
input = sys.stdin.readline

n = int(input())
mid = []
for _ in range(n):
  nums = sorted(map(int, input().split()))
  mid.append(nums[len(nums) // 2])
mid.sort()

ans = mid[len(mid) // 2]
print(ans)