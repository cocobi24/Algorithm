# https://www.acmicpc.net/problem/12033

import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
  n = int(input())
  price = list(map(int, input().split()))

  sales = []
  for _ in range(n):
    sale = price.pop()*0.75
    if sale in price:
      price.remove(sale)
      sales.append(int(sale))

  sales = sales[::-1]
  print(f'Case #{i+1}:', end=' ')
  print(*sales)