# https://www.acmicpc.net/problem/13717

import sys
input = sys.stdin.readline
n = int(input())
max_up = 0
pokemon = ''
cnt = 0

for _ in range(n):
  name = input().rstrip()
  req, item = map(int, input().split())

  up = (item-req)//(req-2)+1
  if up > max_up:
    max_up = up
    pokemon = name
  if up > 0:
    cnt += up
print(cnt, pokemon, sep='\n')