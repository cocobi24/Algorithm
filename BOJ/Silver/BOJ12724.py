# https://www.acmicpc.net/problem/12724

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  n = int(input())
  v1 = sorted(map(int, input().split()))
  v2 = sorted(map(int, input().split()), reverse=True)
  ans = 0
  for j in range(n):
    ans += v1[j] * v2[j]
  print(f"Case #{i+1}: {ans}")