# https://www.acmicpc.net/problem/1009

N = int(input())
direction = list(input().rstrip())

coordinate = set()
coordinate.add((0, 0))
now = [0, 0]
for d in direction:
  if d == "N":
    now[1] += 1
  if d == "E":
    now[0] += 1
  if d == "W":
    now[0] -= 1
  if d == "S":
    now[1] -= 1
  coordinate.add(tuple(now))
print(len(coordinate))