# https://www.acmicpc.net/problem/28431

footwear = []
for _ in range(5):
  n = int(input())
  if n not in footwear:
    footwear.append(n)
  else:
    footwear.remove(n)
print(*footwear)