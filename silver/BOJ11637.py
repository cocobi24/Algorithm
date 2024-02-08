# https://www.acmicpc.net/problem/11637

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  candidate = [0] * n
  total = 0
  for i in range(n):
    candidate[i] = int(input())
    total += candidate[i]

  max_vote = max(candidate)
  mid_vote = total // 2

  if candidate.count(max_vote) > 1:
    print("no winner")
  else:
    R = candidate.index(max_vote) + 1
    if max_vote > mid_vote:
      print(f"majority winner {R}")
    else:
      print(f"minority winner {R}")