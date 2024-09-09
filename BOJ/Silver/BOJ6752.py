# https://www.acmicpc.net/problem/6752

import sys
input = sys.stdin.readline

T = int(input())
C = int(input())
chore = sorted(int(input()) for _ in range(C))
time, cnt = 0, 0
for i in range(C):
  time += chore[i]
  if time > T:
    break
  cnt += 1
print(cnt)