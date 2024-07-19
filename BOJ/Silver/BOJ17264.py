# https://www.acmicpc.net/problem/17264

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
W, L, G = map(int, input().split())
player_info = {}

for _ in range(P):
  name,  res = map(str, input().rstrip().split())
  player_info[name] = res

iron, score = True, 0
for _ in range(N):
  if score >= G:
    iron = False
    break

  player = input().rstrip()

  if player in player_info:
    if player_info[player] == "W":
      score += W
    elif player_info[player] == "L":
      score -= L
  else:
    score -= L

  if score < 0:
    score = 0
print("I AM IRONMAN!!" if iron else "I AM NOT IRONMAN!!")