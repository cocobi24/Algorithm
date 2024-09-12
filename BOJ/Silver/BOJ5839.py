# https://www.acmicpc.net/problem/5839

import sys
input = sys.stdin.readline

def runnig(time):
  recode, run = [], 0
  for _ in range(time):
    speed, time = list(map(int, input().split()))
    for _ in range(time):
      run += speed
      recode.append(run)
  return recode

N, M = map(int, input().split())
bessie = runnig(N)
elsie = runnig(M)

cnt = 0
front = 'bessie' if bessie[0] > elsie[0] else 'elsie'
for i in range(1, len(bessie)):
  if front == 'bessie' and bessie[i] < elsie[i]:
    front = 'elsie'
    cnt += 1
  elif front == 'elsie' and bessie[i] > elsie[i]:
    front = 'bessie'
    cnt += 1
print(cnt)