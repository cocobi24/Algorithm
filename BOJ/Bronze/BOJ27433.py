# https://www.acmicpc.net/problem/27433

n = int(input())

if n == 0 or n == 1:
  print(1)
else:
  fact = 1
  for i in range(2, n + 1):
    fact *= i
  print(fact)