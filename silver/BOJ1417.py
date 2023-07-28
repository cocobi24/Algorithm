# https://www.acmicpc.net/problem/1417

import sys
input = sys.stdin.readline

n = int(input())
vote_list = [int(input()) for _ in range(n)]
dasome, answer = vote_list[0], 0
vote_list = sorted(vote_list[1:], reverse=True)

if n > 1:
  while vote_list[0] >= dasome:
      dasome += 1
      answer += 1
      vote_list[0] -= 1
      vote_list.sort(reverse=True)

print(answer)