# https://www.acmicpc.net/problem/1032

import sys
input = sys.stdin.readline
n = int(input())
files = [list(input().rstrip()) for _ in range(n)]

l = len(files[0])
for i in range(l):
  check = True
  temp = files[0][i]
  for j in range(n):
    if temp != files[j][i]:
      check = False
      break
  print(temp if check else '?', end='')