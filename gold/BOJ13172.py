# https://www.acmicpc.net/problem/13172

import sys
input = sys.stdin.readline
M = int(input())

mod = int(1e9+7)
def calculator(n, x):
  if x == 1:
    return n
  v = calculator(n, x//2)
  if x % 2 == 0:
    return v * v % mod
  return v * v * n % mod

answer = 0
for i in range(M):
  N, S = map(int, input().split())
  calc = calculator(N, mod - 2)
  answer = (answer + calc * S % mod) % mod
print(answer)