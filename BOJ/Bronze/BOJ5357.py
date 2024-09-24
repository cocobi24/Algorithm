# https://www.acmicpc.net/problem/5357

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  s = list(input().rstrip())
  ans = [s[0]]
  for i in range(1, len(s)):
    if s[i] != s[i-1]:
      ans.append(s[i])
  print(*ans, sep='')