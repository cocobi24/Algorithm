# https://www.acmicpc.net/problem/27674

n = int(input())
for _ in range(n*2):
  num = input().rstrip()
  if num == '':
    continue
  nums = sorted(num, reverse=True)
  if len(nums) == 2:
    print(int(nums[0]) + int(nums[1]))
  else:
    a = int(nums.pop())
    print(int(''.join(nums)) + a)