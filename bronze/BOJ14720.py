# https://www.acmicpc.net/problem/14720

n = int(input())
milks = list(map(int, input().split()))
target, cnt = 0, 0
for milk in milks:
  if target == milk:
    cnt += 1
    target += 1
    if target == 3:
      target = 0
print(cnt)