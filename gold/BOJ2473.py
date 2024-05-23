# https://www.acmicpc.net/problem/2473

n = int(input())
nums = sorted(map(int,input().split()))
res = [1e9+1] * 3
ans = []

for i in range(n):
  l, r = i + 1, n - 1
  while l < r:
    if abs(sum(res)) > abs(nums[i] + nums[l] + nums[r]):
      res = [nums[i], nums[l], nums[r]]

    if nums[i] + nums[l] + nums[r] == 0:
      ans = [nums[i], nums[l], nums[r]]
      break
    elif nums[i] + nums[l] + nums[r] > 0:
      r -= 1
    else:
      l += 1
  if ans:
    break

if ans:
  print(*ans)
else:
  print(*res)