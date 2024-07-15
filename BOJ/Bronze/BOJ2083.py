# https://www.acmicpc.net/problem/2083

import sys
input = sys.stdin.readline

while True:
  man = input().rstrip()
  if man == '# 0 0':
    break
  name, age, weight = list(man.split())
  div = "Senior" if int(age) > 17 or int(weight) >= 80 else "Junior"
  print(name, div)