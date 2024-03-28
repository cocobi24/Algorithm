# https://www.acmicpc.net/problem/30457

n = int(input())
rows = sorted(map(int, input().split()))
if n == 1:
  print(1)
else:
  l, r, cnt = rows[0], rows[1], 2
  for row in rows[2:]:
    if row > l:
      l = row
      cnt += 1
    elif row > r:
      r = row
      cnt += 1
  print(cnt)