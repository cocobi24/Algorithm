# https://www.acmicpc.net/problem/1283

import sys
input = sys.stdin.readline

n = int(input())
shotcut_set = set()

for _ in range(n):
  s = input().rstrip()
  ss = s.split()

  for i in range(len(ss)):
    if ss[i][0].upper() not in shotcut_set:
      shotcut_set.add(ss[i][0].upper())
      shotcut = ss[i][0]
      idx = len(''.join(ss[:i])) + i * 1
      break
    shotcut = ''

  if shotcut == '':
    for i in range(len(s)):
      if s[i] != ' ' and s[i].upper() not in shotcut_set:
        shotcut_set.add(s[i].upper())
        shotcut = s[i]
        break
    idx = s.index(shotcut)
  s = list(s)
  s[idx] = f'[{shotcut}]' if shotcut else s[idx]
  print(*s, sep='')