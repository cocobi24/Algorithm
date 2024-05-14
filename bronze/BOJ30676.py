# https://www.acmicpc.net/problem/30676

def getColor(n):
  if 620 <= n <= 780:
    return "Red"
  if 590 <= n <= 7620:
    return "Orange"
  if 570 <= n <= 590:
    return "Yellow"
  if 495 <= n <= 570:
    return "Green"
  if 450 <= n <= 495:
    return "Blue"
  if 425 <= n <= 450:
    return "Indigo"
  if 380 <= n <= 425:
    return "Violet"

color = getColor(int(input()))
print(color)