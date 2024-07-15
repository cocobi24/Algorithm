# https://www.acmicpc.net/problem/5566

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]

cnt, now = 0, 0
for i in range(M):
  cnt += 1
  now += int(input())
  if now >= N: break
  now += board[now]
  if now >= N: break
print(cnt)