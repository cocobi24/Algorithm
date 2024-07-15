# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
nations.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
target = nations[[nations[i][0] for i in range(N)].index(K)][1:]
for i in range(N):
  if nations[i][1:] == target:
    print(i + 1)
    break