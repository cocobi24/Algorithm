# https://www.acmicpc.net/problem/19637

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
title = list(list(map(str, input().split())) for _ in range(N))

hp_list = [int(input()) for _ in range(M)]
for hp in hp_list:
  left, right, idx = 0, N, 0
  while left <= right:
    mid = (left + right) // 2
    if int(title[mid][1]) >= hp:
      right = mid - 1
      idx = mid
    else:
      left = mid + 1
  print(title[idx][0])