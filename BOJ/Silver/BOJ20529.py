# https://www.acmicpc.net/problem/20529

import sys
from itertools import combinations
input = sys.stdin.readline
MBTI = {'E': 1, 'I': 0,
        'S': 1, 'N': 0,
        'F': 1, 'T': 0,
        'P': 1, 'J': 0
        }
T = int(input())

for _ in range(T):
  n = int(input())
  mbti_list = list(map(str, input().split()))
  if n > 32:
    print(0)
  else:
    comb_mbti = list(combinations(mbti_list, 3))
    answer = 9999
    for A, B, C in comb_mbti:
      A, B, C = list(A), list(B), list(C)
      distance = 0
      for i in range(4):
        distance += abs(MBTI[A[i]]-MBTI[B[i]]) + abs(MBTI[B[i]]-MBTI[C[i]]) + abs(MBTI[C[i]]-MBTI[A[i]])
      answer = min(answer, distance)
    print(answer)