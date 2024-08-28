# https://www.acmicpc.net/problem/16283

a, b, n, w = map(int, input().split())
answer = []
for i in range(1, n):
  chlorine, cow = i, n - i
  total = chlorine * a + cow * b
  if total == w:
    answer.append([chlorine, cow])

if len(answer) == 1:
  print(*answer[0])
else:
  print(-1)