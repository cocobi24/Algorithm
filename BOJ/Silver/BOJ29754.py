# https://www.acmicpc.net/problem/29754

import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
weeks = []
for _ in range(M//7):
  weeks.append({})

for _ in range(N):
  name, day, start, end = map(str, input().rstrip().split())
  week = math.ceil(int(day) / 7) - 1
  hh1, mm1 = map(int, start.split(':'))
  hh2, mm2 = map(int, end.split(':'))

  hour = hh2 - hh1 if mm2 > mm1 else hh2 - hh1 - 1
  minute = mm2 - mm1 if mm2 > mm1 else  mm2 - mm1 + 60
  time = hour * 60 + minute
  if name not in weeks[week]:
    weeks[week][name] = [name, 1, time]
  else:
    weeks[week][name][1] += 1
    weeks[week][name][2] += time

answer = set(map(lambda x: x[0], list(filter(lambda x: (x[1] >= 5 and x[2] >= 3600), weeks[0].values()))))
for i in range(1, M//7):
  weeks[i] = set(map(lambda x: x[0], list(filter(lambda x: (x[1] >= 5 and x[2] >= 3600), weeks[i].values()))))
  answer = answer & weeks[i]
answer = sorted(answer)
if len(answer) > 0:
  print(*answer, sep='\n')
else:
  print(-1)