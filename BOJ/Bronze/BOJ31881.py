# https://www.acmicpc.net/problem/31881

import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

infection = set()
for _ in range(Q):
  c = input().rstrip()
  if len(c) > 1:
    c, x = map(int, c.split())
  c = int(c)

  if c == 1:
    infection.add(x)
  elif c == 2 and x in infection:
    infection.remove(x)
  elif c == 3:
    print(N - len(infection))
