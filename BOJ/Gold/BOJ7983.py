# https://www.acmicpc.net/problem/7983

import sys
input = sys.stdin.readline

n = int(input())
works = list(list(map(int, input().split())) for _ in range(n))
works.sort(key=lambda x: (-x[1]))

day = works[0][1]
for i in range(n):
  start = works[i][0]
  end = works[i][1]
  day = end - start if day >= end else day - start

print(day)