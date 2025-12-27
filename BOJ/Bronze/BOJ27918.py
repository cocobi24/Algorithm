# https://www.acmicpc.net/problem/27918

import sys
input = sys.stdin.readline

N = int(input())
score = [0, 0]
for _ in range(N):
  winner = input().rstrip()
  if max(score) - min(score) == 2:
    break
  if winner == "D":
    score[0] += 1
  else:
    score[1] += 1
print(score[0], score[1], sep=':')