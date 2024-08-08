# https://www.acmicpc.net/problem/27161

import sys
input = sys.stdin.readline

N = int(input())
card_list = [list(input().rstrip().split()) for _ in range(N)]

time, d = 0, 'r'
for card in card_list:
  S, X = card[0], int(card[1])
  if d == 'r':
    time += 1
    if time == 13:
      time = 1
  if d == 'l':
    time -= 1
    if time == 0:
      time = 12

  if S != 'HOURGLASS' and X == time:
    print(f'{time} YES')
  else:
    if S == 'HOURGLASS'  and X != time:
      d = 'l' if d == 'r' else 'r'
    print(f'{time} NO')