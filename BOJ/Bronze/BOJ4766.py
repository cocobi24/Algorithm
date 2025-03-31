# https://www.acmicpc.net/problem/4766

init = float(input())
while True:
  n = float(input())
  if n == 999:
    break
  print(f"{round(n - init, 2):.2f}")
  init = n