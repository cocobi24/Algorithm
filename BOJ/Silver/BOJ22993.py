# https://www.acmicpc.net/problem/22993

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
junwon = nums[0]
nums = sorted(nums[1::])
ans = "Yes"
for i in range(n - 1):
  if junwon > nums[i]:
    junwon += nums[i]
  else:
    ans = "No"
    break
print(ans)