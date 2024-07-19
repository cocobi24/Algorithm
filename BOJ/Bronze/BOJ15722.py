# https://www.acmicpc.net/problem/15722

n = int(input())
move = 0
init = [0, 1]
direct = 'E'
if n == 0:
  print(0, 0)
else :
  while move != n - 1:
    move += 1
    if direct == 'N':
      init[1] += 1
      if -init[0] + 1 == init[1]:
        direct = 'E'
    elif direct == 'E':
      init[0] += 1
      if init[0] == init[1]:
        direct = 'S'
    elif direct == 'S':
      init[1] -= 1
      if init[0] == -init[1]:
        direct = 'W'
    elif direct == 'W':
      init[0] -= 1
      if init[0] == init[1]:
        direct = 'N'

  print(*init)