# https://www.acmicpc.net/problem/10174

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  s = input().upper().replace("\n", "")
  print("Yes" if s == s[::-1] else "No")