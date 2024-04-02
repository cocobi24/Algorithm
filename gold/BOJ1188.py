# https://www.acmicpc.net/problem/1188

import sys
input = sys.stdin.readline

def gcd(a, b):
  if a % b == 0:
    return b
  return gcd(b, a % b)

N, M = map(int, input().split())
ans = M - gcd(N, M)
print(ans)