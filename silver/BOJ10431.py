# https://www.acmicpc.net/problem/10431

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  line = list(map(int, input().split()))
  idx, line = line[0], line[1::]
  cnt = 0
  for i in range(1, len(line)):
    for j in range(i):
      if line[j] > line[i]:
        cnt += 1
  print(idx, cnt)