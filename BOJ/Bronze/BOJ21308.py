# https://www.acmicpc.net/problem/21308

n = int(input())
for i in range(n * 2):
  print(f"{'@' * n}{' ' * n * 3}{'@' * n}")
for i in range(n):
  print("@" * (n * 5))
for i in range(n):
  print(f"{'@' * n}{' ' * n * 3}{'@' * n}")
for i in range(n):
  print("@" * (n * 5))