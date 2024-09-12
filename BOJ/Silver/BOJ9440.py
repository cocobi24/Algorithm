# https://www.acmicpc.net/problem/9440

import sys
input = sys.stdin.readline

while True:
  nums = list(map(int, input().split()))

  if nums[0] == 0:
    break
  nums = sorted(nums[1::], reverse=True)

  zero = []
  if 0 in nums:
    for _ in range(nums.count(0)):
      zero.append(nums.pop())

  a, b = [nums.pop()], [nums.pop()]
  while zero:
    a.append(zero.pop())
    if zero:
      b.append(zero.pop())

  if len(a) <= len(b):
    while nums:
      a.append(nums.pop())
      if nums:
        b.append(nums.pop())
  else:
    while nums:
      b.append(nums.pop())
      if nums:
        a.append(nums.pop())

  a = int(''.join(map(str, a)))
  b = int(''.join(map(str, b)))
  print(a + b)