# https://www.acmicpc.net/problem/21557

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
i = N - 2
while i > 0:
  if i == 1:
    A[0] -= 1
    A[-1] -= 1
  else:
    if A[0] >= A[-1]:
      A[0] -= 1
    else:
      A[-1] -= 1
  i -= 1
print(max(A[0], A[-1]))