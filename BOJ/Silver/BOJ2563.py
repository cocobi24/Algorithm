# https://www.acmicpc.net/problem/2563

import sys
input = sys.stdin.readline
n = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(n):
  a, b = map(int, input().split())
  for i in range(a, a+10):
    for j in range(b, b+10):
      paper[i][j] = 1

ans = sum(sum(i) for i in paper)
print(ans)