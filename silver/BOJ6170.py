# https://www.acmicpc.net/problem/6170

def solve(n):
  if n == 1:
    return 2

  if n == 2:
    return 3
  a, b = 2, 3
  for _ in range(2, n):
    a, b = b, a + b
  return b


T= int(input())
for i in range(T):
  n = int(input())
  print(f"Scenario #{i+1}:")
  print(solve(n))
  if i == T - 1:
    break
  print()