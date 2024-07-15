# https://www.acmicpc.net/problem/15905

import sys
input = sys.stdin.readline
n = int(input())
score = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))

if n <= 5:
  print(0)
else:
  target = score[4][0]
  ans = list(filter(lambda x: x[0] == target, score[5:]))
  print(len(ans))