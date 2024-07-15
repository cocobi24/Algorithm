# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans, temp = 0, []

def solve(s):
  global ans
  if sum(temp) == S and len(temp) > 0:
    ans += 1

  for i in range(s, N):
    temp.append(nums[i])
    solve(i+1)
    temp.pop()

solve(0)
print(ans)