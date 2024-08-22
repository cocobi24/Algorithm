# https://www.acmicpc.net/problem/10193

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  origin, target = map(str, input().rstrip().split())
  l = len(origin)
  cost = 0
  for i in range(l):
    ord_origin = ord(origin[i])
    ord_target = ord(target[i])
    if ord_origin < ord_target:
      cost -= ord_target - ord_origin
    elif ord_origin > ord_target:
      cost += ord_origin - ord_target
  if cost == 0:
    cost = "was FREE."
  elif cost > 0:
    cost = f"earned {cost} coins."
  else:
    cost = f"cost {abs(cost)} coins."
  print(f"Swapping letters to make {origin} look like {target} {cost}")