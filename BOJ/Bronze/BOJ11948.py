# https://www.acmicpc.net/problem/11948

import sys
input = sys.stdin.readline
score = []
for _ in range(6):
  score.append(int(input()))
print(sum(sorted(score[0:4])[1:]) + max(sorted(score[4:6])))