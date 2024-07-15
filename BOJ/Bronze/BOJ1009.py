# https://www.acmicpc.net/problem/1009

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  a %= 10

  if a == 0:
    print(10)
  elif a in [1, 5, 6]:
    print(a)
  elif a in [4, 9]:
    print(a if b % 2 == 1 else (a * a) % 10)
  else:
    print((a ** 4) % 10 % 10 % 10 if b % 4 == 0 else (a ** b) % 10 % 10 % 10)