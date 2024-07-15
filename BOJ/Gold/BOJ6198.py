# https://www.acmicpc.net/problem/6198

import sys
input = sys.stdin.readline
N = int(input())
H = [int(input()) for _ in range(N)]

stack, ans = [], 0
for h in H:
  while stack and stack[-1] <= h:
    stack.pop()
  stack.append(h)
  ans += len(stack)-1

print(ans)