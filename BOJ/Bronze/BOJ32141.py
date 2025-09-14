# https://www.acmicpc.net/problem/32141

N, H = map(int, input().split())
d = map(int, input().split())

power, cnt = 0, 0
for i in d:
  cnt += 1
  power += i
  if power >= H:
    break
print(cnt if power >= H else -1)