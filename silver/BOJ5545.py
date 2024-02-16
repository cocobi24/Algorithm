# https://www.acmicpc.net/problem/5545

import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
C = int(input())
D = sorted([int(input()) for _ in range(N)], reverse=True)

kcal, cost = C, A
value = int(kcal / cost)
for i in range(N):
  newValue = int((kcal + D[i]) / (cost + B))
  if newValue >= value:
    kcal += D[i]
    cost += B
    value = newValue
  else:
    break
print(value)