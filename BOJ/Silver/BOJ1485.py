# https://www.acmicpc.net/problem/1485

import sys
input = sys.stdin.readline
T = int(input())

def line_length(x, y):
  return abs(x[0]-y[0])**2 + abs(x[1]-y[1])**2

for _ in range(T):
  square = []
  for _ in range(4):
    x, y = map(int, input().split())
    square.append((x,y))
  square = sorted(square)

  coordinate = []
  for i in range(3):
    for j in range(i, 4):
      if i != j:
        coordinate.append(line_length(square[i], square[j]))

  uniq = len(set(coordinate))
  max_cnt = coordinate.count(max(coordinate))
  min_cnt = coordinate.count(min(coordinate))
  print(1 if uniq == 2 and max_cnt == 2 and min_cnt == 4 else 0)