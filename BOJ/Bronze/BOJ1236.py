# https://www.acmicpc.net/problem/1236

import sys
input = sys.stdin.readline
x, y = list(map(int ,input().split()))

castle_row = [input().rstrip() for _ in range(x)]
cnt_row = 0
for i in range(x):
  if 'X' not in castle_row[i]:
    cnt_row += 1

cnt_col = 0
for i in range(y):
  col = ''
  for j in range(x):
    col += castle_row[j][i]
  if 'X' not in col:
    cnt_col += 1

print(max(cnt_row, cnt_col))