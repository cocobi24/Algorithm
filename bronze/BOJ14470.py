# https://www.acmicpc.net/problem/14470

import sys
input = sys.stdin.readline
option = [int(input()) for _ in range(5)]
A, B, C, D, E = option

time = 0
if A < 0 :
  time += abs(A) * C + D + B * E
else :
  time += (B - A) * E
print(time)