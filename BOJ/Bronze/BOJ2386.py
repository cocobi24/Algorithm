# https://www.acmicpc.net/problem/2386

import sys
input = sys.stdin.readline

while True:
  s = input().rstrip()
  if s == '#':
    break
  alpha = s[0]
  parnassus = s[2:]
  print(s[0], parnassus.count(alpha) + parnassus.count(alpha.upper()))