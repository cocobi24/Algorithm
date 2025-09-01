# https://www.acmicpc.net/problem/265530

n = int(input())
for _ in range(n):
  x = int(input())
  cost = 0
  for i in range(x):
    item, qtt, c = map(str, input().split())
    if c[0] == '.':
      c = '0' + c
    cost += int(qtt) * float(c)
  print(f'${cost:.2f}')