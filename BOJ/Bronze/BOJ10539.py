# https://www.acmicpc.net/problem/10539

n = int(input())
nums = list(map(int, input().split()))

ans = [nums[0]]
for i in range(1, n):
  ans.append(nums[i] * (i+1) - sum(ans))
print(*ans)