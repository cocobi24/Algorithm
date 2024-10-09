# https://www.acmicpc.net/problem/5523

import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * 2
for _ in range(n):
  a, b = map(int, input().split())
  if a > b:
    ans[0] += 1
  elif b > a:
    ans[1] += 1
print(*ans)