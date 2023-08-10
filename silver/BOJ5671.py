# https://www.acmicpc.net/problem/5671

import sys
input = sys.stdin.readline

for input in sys.stdin:
  n, m = map(int, input.rstrip().split())
  answer = 0

  for i in range(n, m+1):
    number = []
    i = list(str(i))
    flag = True
    for s in i:
      if s in number:
        flag = False
        break
      else:
        number.append(s)
    if flag:
      answer += 1

  print(answer)