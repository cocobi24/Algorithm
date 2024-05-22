# https://www.acmicpc.net/problem/5717

while True:
  man = sum(map(int, input().split()))
  if man == 0:
    break
  print(man)