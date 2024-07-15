# https://www.acmicpc.net/problem/1895

import sys
input = sys.stdin.readline
r, c = map(int, input().split())

image = []
for i in range(r) :
  image.append(list(map(int, input().split())))

filter_list = []
for i in range(r-2) :
  for j in range(c-2):
    ft = sorted([
      image[i][j], image[i][j+1], image[i][j+2],
      image[i+1][j], image[i+1][j + 1], image[i+1][j + 2],
      image[i+2][j], image[i+2][j + 1], image[i+2][j + 2]
    ])
    filter_list.append(ft[4])

t = int(input())
answer = 0
for i in range(len(filter_list)) :
  if filter_list[i] >= t :
    answer += 1

print(answer)