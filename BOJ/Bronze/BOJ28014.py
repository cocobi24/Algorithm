# https://www.acmicpc.net/problem/28014

n = int(input())
nums = list(map(int, input().split()))
ans = 1
for i in range(n - 1):
  if nums[i+1] >= nums[i]:
    ans += 1
print(ans)