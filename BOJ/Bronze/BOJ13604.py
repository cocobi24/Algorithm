# https://www.acmicpc.net/problem/13604

player, round = map(int, input().split())
gemes = list(map(int, input().split()))
score = [0] * player

idx = 0
for i in range(0, player*round):
  if idx >= player:
    idx = 0

  score[idx] += gemes[i]
  idx += 1

print(len(score) - score[::-1].index(max(score)))