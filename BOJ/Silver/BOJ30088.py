# https://www.acmicpc.net/problem/30088

import sys
input = sys.stdin.readline

n = int(input())
team_list = []
for _ in range(n):
  team = list(map(int, input().split()))
  _ = 0
  for i in range(1, team[0]+1):
    _ += team[i]
  team_list.append(_)
team_list.sort()

temp, answer = team_list[0], team_list[0]
for i in range(1, n):
  temp += team_list[i]
  answer += temp
print(answer)