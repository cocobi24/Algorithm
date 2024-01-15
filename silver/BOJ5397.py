# https://www.acmicpc.net/problem/5397

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  str = list(input().rstrip())
  ans, temp = [], []
  for s in str:
    if s == '<':
      if len(ans) > 0:
        c = ans.pop()
        temp.append(c)
    elif s == '>':
      if len(temp) > 0:
        c = temp.pop()
        ans.append(c)
    elif s == '-':
      if len(ans) > 0:
        ans.pop()
    else:
      ans.append(s)
  ans += temp[::-1]
  print(''.join(ans))