# https://www.acmicpc.net/problem/2508

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
  input()
  r, c = map(int, input().split())

  candy_list = []
  for i in range(r) :
    candy_list.append([])
    rows = list(input())
    for cell in rows :
      candy_list[i].append(cell)

  cnt = 0
  for i in range(r) :
    for j in range(c) :
      if j < c-2 and candy_list[i][j] == '>' :
        candy = candy_list[i][j] + candy_list[i][j+1] + candy_list[i][j+2]
        if candy == '>o<' :
          cnt += 1
      if i < r-2 and candy_list[i][j] == 'v' :
        candy = candy_list[i][j] + candy_list[i+1][j] + candy_list[i+2][j]
        if candy == 'vo^' :
          cnt += 1
  print(cnt)