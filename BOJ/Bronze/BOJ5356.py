# https://www.acmicpc.net/problem/5356

import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
  num, s = input().rstrip().split()
  num = int(num)
  ord_num = ord(s)
  for i in range(1, num + 1):
    print(chr(ord_num) * i)
    ord_num += 1
    if ord_num > 90:
      ord_num = 65
  print()