# https://www.acmicpc.net/problem/11292

import sys
input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0 :
    break

  answer, max_h = [], 0
  for _ in range(n):
    name, height = input().split()
    height = float(height)
    if height > max_h:
      max_h = height
      answer = [name]
    elif height == max_h:
      answer.append(name)
  print(*answer)
