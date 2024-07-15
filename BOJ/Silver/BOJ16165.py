# https://www.acmicpc.net/problem/16165

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

team_name, name_team = {}, {}
for _ in range(n):
  team = input().rstrip()
  t = int(input())
  team_name[team] = set()

  for _ in range(t):
    name = input().rstrip()
    team_name[team].add(name)
    name_team[name] = team

for _ in range(m):
  quiz_name = input().rstrip()
  quiz_type = int(input().rstrip())
  if quiz_type == 1:
    print(name_team[quiz_name])
  else:
    print(*sorted(team_name[quiz_name]), sep='\n')