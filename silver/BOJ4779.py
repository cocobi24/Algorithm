# https://www.acmicpc.net/problem/4779

import sys
input = sys.stdin

def cantorian_set(l):
  if l == 1:
    print('-', end='')
  else:
    cantorian_set(l//3)
    print(' ' * (l//3), end='')
    cantorian_set(l//3)

for n in input:
  n = int(n.rstrip())
  cantorian_set(3**n)
  print()