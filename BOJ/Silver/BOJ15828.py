# https://www.acmicpc.net/problem/15828

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
router = deque()

while True:
  packet = int(input())
  if packet == -1:
    break

  if packet == 0:
    router.popleft()
  elif len(router) < N:
    router.append(packet)

if len(router) > 0:
  print(*router)
else:
  print("empty")