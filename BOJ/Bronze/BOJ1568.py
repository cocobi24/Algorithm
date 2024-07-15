# https://www.acmicpc.net/problem/1568

n = int(input())
idx, cnt = 1, 0

while True:
  if n == 0:
    break
  cnt += 1
  n -= idx
  if n < 0:
    n += idx
    idx = 1
    cnt -= 1
  else:
    idx += 1

print(cnt)