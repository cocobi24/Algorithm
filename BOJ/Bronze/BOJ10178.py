# https://www.acmicpc.net/problem/10178

T = int(input())

for _ in range(T):
  c, v = map(int, input().split())
  you, dad = c // v, c % v
  print(f"You get {you} piece(s) and your dad gets {dad} piece(s).")