# https://www.acmicpc.net/problem/16917

A, B, C, X, Y = map(int, input().split())
C *= 2
money = 0
if A + B > C:
  m = min([X, Y])
  X, Y = X - m, Y - m
  if A > C and B > C:
    money = (C * X) + (C * Y) + (C * m)
  elif A > C:
    money = (C * X) + (B * Y) + (C * m)
  elif B > C :
    money = (A * X) + (C * Y) + (C * m)
  else :
    money = (A * X) + (B * Y) + (C * m)
else:
  money = (A * X) + (B * Y)
print(money)