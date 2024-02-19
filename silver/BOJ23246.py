# https://www.acmicpc.net/problem/23246

import sys
input = sys.stdin.readline
n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  score[i].append(score[i][1] * score[i][2] * score[i][3])
  score[i].append(score[i][1] + score[i][2] + score[i][3])
score.sort(key=lambda x:(x[4], x[5], x[0]))
print(score[0][0], score[1][0], score[2][0])