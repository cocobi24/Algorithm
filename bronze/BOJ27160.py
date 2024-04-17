# https://www.acmicpc.net/problem/27160

import sys
input = sys.stdin.readline

n = int(input())
fruits = {}
for _ in range(n):
  f, ea = map(str, input().rstrip().split())
  ea = int(ea)
  if f in fruits :
    fruits[f] += ea
  else:
    fruits[f] = ea

flag = False
for f in fruits.items():
  if f[1] == 5:
    flag = True
    break

print("YES" if flag else "NO")