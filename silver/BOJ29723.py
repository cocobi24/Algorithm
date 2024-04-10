# https://www.acmicpc.net/problem/29723

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
sub_set = {}
for _ in range(N):
  sub, score = map(str, input().rstrip().split())
  sub_set[sub] = int(score)

base = 0
for _ in range(K):
  public_sub = input().rstrip()
  base += sub_set[public_sub]
  del sub_set[public_sub]

scores = list(sub_set.values())
scores.sort()
scores_rev = scores.copy()
scores_rev.reverse()

min_score = 0
max_score = 0
for i in range(M-K):
  min_score += scores[i]
  max_score += scores_rev[i]
print(base + min_score, base + max_score)