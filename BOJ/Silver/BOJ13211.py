# https://www.acmicpc.net/problem/13211

import sys
input = sys.stdin.readline
n = int(input())
steal = set(input().rstrip() for _ in range(n))
m = int(input())

cnt = 0
for _ in range(m):
  passport = input().rstrip()
  cnt += 1 if passport in steal else 0
print(cnt)