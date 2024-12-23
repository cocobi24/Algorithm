# https://www.acmicpc.net/problem/11235

import sys
input = sys.stdin.readline

n = int(input())
vote = {}
max_vote = 0
for _ in range(n):
  name = input().rstrip()
  if name not in vote:
    vote[name] = [name, 1]
  else:
    vote[name][1] += 1
  if vote[name][1] > max_vote:
    max_vote = vote[name][1]

vote_list = sorted(filter(lambda x: x[1] == max_vote, vote.values()))
for i in vote_list:
  print(i[0])