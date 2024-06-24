# https://www.acmicpc.net/problem/2526

n, p = map(int, input().split())
nums, num = [], n * n

while True:
  mod = num % p
  num = mod * n

  if mod in nums:
    break

  nums.append(mod)
print(len(nums) - nums.index(mod))