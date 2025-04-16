# https://www.acmicpc.net/problem/25400

n = int(input())
cards = list(map(int, input().split()))

target,count = 1, 0
for card in cards:
  if card == target:
    target += 1
  else:
    count += 1
print(count)