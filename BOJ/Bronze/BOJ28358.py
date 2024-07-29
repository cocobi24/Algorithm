# https://www.acmicpc.net/problem/28358

import sys
input = sys.stdin.readline

T = int(input())
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = []
for i in range(1, 13):
  for n in range(1, month[i] + 1):
    days.append(f"{i}{n}")

for _ in range(T):
  nums = list(map(int, input().split()))
  expect = days.copy()
  for i in range(10):
    if nums[i] == 1:
      expect = list(filter(lambda x: (str(i) not in x), expect))
  print(len(expect))