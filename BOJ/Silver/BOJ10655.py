# https://www.acmicpc.net/problem/10655

import sys
input = sys.stdin.readline
n = int(input())
route = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n-1):
  x1, y1 = route[i]
  x2, y2 = route[i + 1]
  total += abs(x1 - x2) + abs(y1 - y2)

answer = 9999999999
for i in range(n-2):
  x1, y1 = route[i]
  x2, y2 = route[i + 1]
  x3, y3 = route[i + 2]
  a = abs(x1 - x2) + abs(y1 - y2)
  b = abs(x2 - x3) + abs(y2 - y3)
  c = abs(x1 - x3) + abs(y1 - y3)
  answer = min(answer, total - a - b + c)

print(answer)