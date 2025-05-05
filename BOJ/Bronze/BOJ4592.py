# https://www.acmicpc.net/problem/4592

while True:
  nums = list(map(int, input().split()))
  if nums[0] == 0:
    break
  ans = [-1]
  for i in range(1, nums[0] + 1):
    if ans[-1] != nums[i]:
      ans.append(nums[i])
  print(*ans[1:], '$')