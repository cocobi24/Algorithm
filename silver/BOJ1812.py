# https://www.acmicpc.net/problem/1812

import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

a = 0
for i in range(1, n+1) :
  if i % 2 == 1 :
    a += nums[i-1]
  else :
    a -= nums[i-1]

a //= 2
print(a)
num = a
for i in range(n-1) :
  num = nums[i] - num
  print(num)