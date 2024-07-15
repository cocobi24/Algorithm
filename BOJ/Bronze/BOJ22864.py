# https://www.acmicpc.net/problem/22864

A, B, C, M = map(int, input().split())

fatigue, ans = 0, 0
if A > M :
  print(ans)
else:
  for _ in range(24):
    if fatigue + A > M:
      fatigue -= C
      if fatigue < 0:
        fatigue = 0
    else:
      ans += B
      fatigue += A
  print(ans)