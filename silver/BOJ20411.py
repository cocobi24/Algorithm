# https://www.acmicpc.net/problem/20411

m, seed, x1, x2 = map(int, input().split())

for a in range(m+1):
  zero = ((seed - x1) * a + x2 - x1) % m

  if zero == 0:
    for c in range(m+1):
      if x2 == (a * x1 + c) % m:
        print(a, c)
        exit(0)