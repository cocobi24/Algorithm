# https://www.acmicpc.net/problem/4539

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  x = list(map(int, input().rstrip()))
  for i in range(len(x)-1, 0, -1):
    if x[i] > 4:
      x[i - 1] += 1
    x[i] = 0
  ans = ''.join(list(map(str, x)))
  print(ans)