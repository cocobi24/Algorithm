# https://www.acmicpc.net/problem/18242

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board, count = [], []
for i in range(N):
  row = input().rstrip()
  if '#' in row:
    board.append(row)
    count.append(row.count('#'))

if count[0] != count[-1]:
  print('UP' if count[0] < count[-1] else 'DOWN')
else:
  idx = count.index(min(count))
  target_1 = board[idx-1].index('#')
  target_2 = board[idx].index('#')
  print('LEFT' if target_1 != target_2 else 'RIGHT')