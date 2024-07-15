# https://www.acmicpc.net/problem/15786

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = input().rstrip()

for _ in range(m):
  post = input().strip()
  ans, idx = False, 0
  for p in post:
    if p == s[idx]:
      idx += 1
    if idx == n:
      ans = True
      break
  print('true' if ans else 'false')