# https://www.acmicpc.net/problem/23795

money = 0
while True:
  n = int(input())
  if n == -1:
    break
  money += n
print(money)