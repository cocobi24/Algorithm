# https://www.acmicpc.net/problem/10214

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  game = [0, 0]
  for _ in range(9):
    y, k = map(int, input().split())
    game[0] += y
    game[1] += k
  if game[0] == game[1]:
    print("Draw")
  else:
    print("Yonsei" if game[0] > game[1] else "Korea")