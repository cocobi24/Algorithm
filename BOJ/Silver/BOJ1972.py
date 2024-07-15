# https://www.acmicpc.net/problem/1972

import sys
input = sys.stdin.readline

char, c = [], ''
while c != '*':
  c = input().rstrip()
  char.append(c)
char.pop()

def search(c):
  for i in range(1, len(c)):
    comb = []
    for j in range(len(c)-1):
      if j+i < len(c):
        s = c[j] + c[j+i]
        if s not in comb:
          comb.append(s)
        else:
          return "is NOT surprising."
  return "is surprising."

for c in char:
  ans = search(c)
  print(c,ans)