# https://www.acmicpc.net/problem/23895

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  n, money = map(int, input().split())
  home = sorted(map(int, input().split()))
  cnt = 0
  for j in range(n):
    money -= home[j]
    if money < 0:
      break
    cnt += 1
  print(f"Case #{i+1}: {cnt}")