# https://www.acmicpc.net/problem/2865

import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
attendants = [list(map(float, input().split())) for _ in range(M)]

answers = [0] * N
for attendant in attendants:
  for idx in range(N):
    i, s = int(attendant[2 * idx]) - 1, float(attendant[2 * idx + 1])
    answers[i] = max(answers[i], s)
print(round(sum(sorted(answers, reverse=True)[:K]), 1))