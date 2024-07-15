# https://www.acmicpc.net/problem/14382

import sys
input = sys.stdin.readline
T = int(input())

for i in range(1, T+1):
  num = int(input())
  number = num
  if num == 0:
    print(f'Case #{i}: INSOMNIA')
  else:
    nums = set()
    idx = 1
    while True:
      for n in list(str(number)):
        if n not in nums:
          nums.add(n)
      if len(nums) == 10:
        break
      idx += 1
      number = num * idx
    print(f'Case #{i}: {number}')