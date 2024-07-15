# https://www.acmicpc.net/problem/5533

import copy
n = int(input())
score = list(list(map(int ,input().split())) for _ in range(n))

temp = []
for i in range(3):
  temp.append([])
  for j in range(n):
    temp[i].append(score[j][i])

score = copy.deepcopy(temp)
for i in range(3):
  for j in range(n):
    if score[i].count(temp[i][j]) > 1:
      temp[i][j] = 0

answer = [0] * n
for i in range(n):
  answer[i] = temp[0][i] + temp[1][i] + temp[2][i]
print(*answer, sep='\n')