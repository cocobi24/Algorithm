# https://www.acmicpc.net/problem/15025

l, r = map(int, input().split())
if l == r == 0:
  print("Not a moose")
else:
  point = "Even" if l == r else "Odd"
  print(point, r * 2 if point == "Even" else max(l, r) * 2)