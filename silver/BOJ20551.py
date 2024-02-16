# https://www.acmicpc.net/problem/20551

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
B = sorted(int(input()) for _ in range(N))

dict = {}
for i in range(N):
  if B[i] not in dict:
    dict[B[i]] =i

for _ in range(M):
  num = int(input())
  print(dict[num] if num in dict else -1 )