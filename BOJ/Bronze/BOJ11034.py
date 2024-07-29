# https://www.acmicpc.net/problem/11034

import sys
input = sys.stdin

while True:
  T = input.readline().rstrip()
  if T == '':
    break
  x, y, z = sorted(map(int, T.split()))
  cnt = 0
  if y - x < z - y:
    while True:
      if y == z:
        break
      temp = y
      x = y
      y += 1
      cnt += 1
  else:
    while True:
      if x == y:
        break
      temp = y
      z = y
      y -= 1
      cnt += 1
  print(cnt - 1)