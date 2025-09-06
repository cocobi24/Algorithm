# https://www.acmicpc.net/problem/10569

T = int(input())

for _ in range(T):
  V, E = map(int, input().split())
  F = 2 - (V - E)
  print(F)