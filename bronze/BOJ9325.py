# https://www.acmicpc.net/problem/9325

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  s = int(input())
  price = s
  option = int(input())
  for _ in range(option):
    p, q = map(int,input().split())
    price += (p*q)
  print(price)