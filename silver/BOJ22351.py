# https://www.acmicpc.net/problem/22351

num = input()
for i in range(1, len(num)+1):
  start = num[:i]
  next = int(start)

  while len(start) < len(num):
    next += 1
    start += str(next)

  if start == num:
    print(num[:i], next)
    break