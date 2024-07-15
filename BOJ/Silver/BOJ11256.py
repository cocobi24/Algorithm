# https://www.acmicpc.net/problem/11256

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  J, N = map(int, input().split())
  boxes = []
  for _ in range(N):
    r, c = map(int, input().split())
    boxes.append(r*c)
  boxes.sort(reverse=True)

  cnt = 0
  for box in boxes:
    cnt += 1
    J -= box
    if J <= 0:
      break
  print(cnt)