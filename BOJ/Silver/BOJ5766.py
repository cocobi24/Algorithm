# https://www.acmicpc.net/problem/5766

import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break

  ranking = {}
  for _ in range(n):
    rank = list(map(int, input().split()))
    for r in rank:
      if r in ranking:
        ranking[r][1] += 1
      else:
        ranking[r] = [r, 0]

  ranking = list(ranking.values())
  ranking.sort(key=lambda x:(-x[1], x[0]))

  top2 = ranking[1][1]
  answer = ''
  for rank in ranking:
    if rank[1] == top2:
      answer += str(rank[0]) + ' '
  print(answer.rstrip())