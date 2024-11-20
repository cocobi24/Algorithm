# https://www.acmicpc.net/problem/17072

import sys
input = sys.stdin.readline

def REFINE_RGB(R, G, B):
  RGB = (2126 * R) + (7152 * G) + (722 * B)
  if 2040000 <= RGB:
    return '.'
  elif 1530000 <= RGB:
    return '-'
  elif 1020000 <= RGB:
    return '+'
  elif 510000 <= RGB:
    return 'o'
  elif 0 <= RGB:
    return '#'

N, M = map(int, input().split())
for _ in range(N):
  row = map(int, input().split())
  line = []
  r, g, b = 0, 0, 0
  for i, v in enumerate(row, 1):
    if i % 3 == 1:
      r = v
    elif i % 3 == 2:
      g = v
    elif i % 3 == 0:
      b = v
      line.append(REFINE_RGB(r, g, b))
  print(*line, sep='')